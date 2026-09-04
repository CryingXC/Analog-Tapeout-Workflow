# Contributing

Contributions are welcome when they improve **process-independent** analog IC implementation methodology.

Before opening a pull request:

1. Do not include PDKs, models, rule decks, techfiles, GDS/OASIS, extracted production netlists or private infrastructure information.
2. Prefer general engineering reasoning over foundry-specific screenshots.
3. State assumptions when a recommendation depends on circuit class, simulator or extraction setup.
4. Run:
   ```bash
   python tools/verify_public_repo.py .
   python -m unittest discover -s tests -v
   ```
5. Keep examples small enough that a reader can understand the failure mechanism without access to proprietary tools.
