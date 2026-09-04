# Public Release Policy

This repository is intentionally designed to be safe for public GitHub use.

## Do not commit
- foundry PDK directories;
- SPICE/model-card files supplied under license;
- Calibre/DRC/LVS/PEX rule decks;
- process techfiles and layer maps;
- GDSII / OASIS;
- production DSPF/SPF/SPEF extracted netlists;
- proprietary standard-cell/device libraries;
- license-server addresses or private infrastructure;
- credentials, tokens or passwords.

## Prefer publishing
- self-drawn architecture diagrams;
- process-independent methodology;
- sanitized plots;
- result summaries;
- debugging logic;
- checklists;
- original scripts that do not embed restricted data.

Run `python tools/verify_public_repo.py .` before publishing, then perform a manual review.
