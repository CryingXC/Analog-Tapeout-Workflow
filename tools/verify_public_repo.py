from __future__ import annotations

import argparse
import re
from pathlib import Path
from urllib.parse import unquote

BANNED_SUFFIXES = {
    '.gds', '.gdsii', '.oas', '.oasis', '.dspf', '.spf', '.spef',
    '.scs', '.cdl', '.tf', '.tech', '.rule', '.rules', '.svdb', '.pex', '.xrc',
}
BANNED_PARTS = {
    'pdk', 'pdks', 'models', 'model', 'rule_decks', 'rule-decks',
    'techfiles', 'extracted', 'netlist', 'private', 'confidential',
}
SECRET_PATTERNS = [
    re.compile(r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----'),
    re.compile(r'(?i)\b(password|passwd|api[_-]?key|access[_-]?token)\s*[:=]\s*["\']?[A-Za-z0-9_\-]{8,}'),
]
LINK_RE = re.compile(r'(?<!!)\[[^\]]+\]\(([^)]+)\)|!\[[^\]]*\]\(([^)]+)\)')


def is_banned_path(path: Path) -> bool:
    lowered_parts = {part.lower() for part in path.parts}
    if lowered_parts & BANNED_PARTS:
        return True
    return path.suffix.lower() in BANNED_SUFFIXES


def iter_files(root: Path):
    for p in root.rglob('*'):
        if p.is_file() and '.git' not in p.parts:
            yield p


def relative_links(md_path: Path):
    text = md_path.read_text(encoding='utf-8', errors='ignore')
    for match in LINK_RE.finditer(text):
        target = match.group(1) or match.group(2)
        if not target:
            continue
        target = target.strip().split('#', 1)[0]
        if not target or target.startswith(('http://', 'https://', 'mailto:', '#')):
            continue
        yield unquote(target)


def verify(root: Path) -> list[str]:
    errors: list[str] = []
    root = root.resolve()
    self_path = Path(__file__).resolve()

    for p in iter_files(root):
        rel = p.relative_to(root)
        if is_banned_path(rel):
            errors.append(f'BANNED PATH: {rel}')

        if p != self_path and p.suffix.lower() in {'.md', '.txt', '.py', '.yml', '.yaml', '.json'}:
            text = p.read_text(encoding='utf-8', errors='ignore')
            for pattern in SECRET_PATTERNS:
                if pattern.search(text):
                    errors.append(f'POSSIBLE SECRET: {rel}')
                    break

        if p.suffix.lower() == '.md':
            for link in relative_links(p):
                target = (p.parent / link).resolve()
                try:
                    target.relative_to(root)
                except ValueError:
                    errors.append(f'LINK ESCAPES REPO: {rel} -> {link}')
                    continue
                if not target.exists():
                    errors.append(f'BROKEN LINK: {rel} -> {link}')

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description='Check a public IC-design repository for unsafe paths and broken relative Markdown links.')
    parser.add_argument('root', nargs='?', default='.')
    args = parser.parse_args()
    errors = verify(Path(args.root))
    if errors:
        print('Public-release verification FAILED')
        for err in errors:
            print(f' - {err}')
        return 1
    print('Public-release verification PASSED')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
