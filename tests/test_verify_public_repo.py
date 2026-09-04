import tempfile
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
import verify_public_repo as v


class VerifyPublicRepoTests(unittest.TestCase):
    def test_rejects_foundry_like_artifact_paths(self):
        self.assertTrue(v.is_banned_path(Path('pdk/device/model.scs')))
        self.assertTrue(v.is_banned_path(Path('layout/top.gds')))
        self.assertTrue(v.is_banned_path(Path('results/extracted/block.dspf')))

    def test_allows_public_markdown_and_python(self):
        self.assertFalse(v.is_banned_path(Path('docs/06-lvs.md')))
        self.assertFalse(v.is_banned_path(Path('tools/verify_public_repo.py')))

    def test_detects_broken_relative_link(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            (root / 'README.md').write_text('[missing](docs/nope.md)\n', encoding='utf-8')
            errors = v.verify(root)
            self.assertTrue(any('BROKEN LINK' in e for e in errors))

    def test_accepts_valid_relative_link(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            (root / 'docs').mkdir()
            (root / 'docs' / 'ok.md').write_text('# ok\n', encoding='utf-8')
            (root / 'README.md').write_text('[ok](docs/ok.md)\n', encoding='utf-8')
            self.assertEqual(v.verify(root), [])


if __name__ == '__main__':
    unittest.main()
