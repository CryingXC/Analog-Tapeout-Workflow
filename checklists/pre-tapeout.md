# Pre-Tapeout Checklist

## Design intent
- [ ] Specification is frozen or changes are explicitly tracked.
- [ ] Top-level block diagram matches the implemented hierarchy.
- [ ] Pin list and polarity are reviewed.
- [ ] Enable/reset/default states are documented.
- [ ] Startup/power sequence is documented.

## Pre-layout verification
- [ ] DC operating point reviewed.
- [ ] Relevant AC/stability checks pass.
- [ ] Startup passes.
- [ ] Functional transient tests pass.
- [ ] PVT matrix reviewed.
- [ ] Monte Carlo completed where mismatch matters.
- [ ] Device stress checks reviewed.

## Physical implementation
- [ ] Final DRC passes under the authorized signoff flow.
- [ ] Final LVS passes under the authorized signoff flow.
- [ ] PEX generated using the intended extraction setup.
- [ ] Top-level supply/ground connectivity reviewed.
- [ ] Pad/pin/package mapping reviewed.

## Post-layout
- [ ] Config/hierarchy view resolution inspected.
- [ ] Critical cells use the intended extracted view.
- [ ] Post-layout metrics compared with pre-layout baseline.
- [ ] Major deltas are explained.
- [ ] Worst-case post-layout results retain acceptable margin.

## Release package
- [ ] Version/tag/commit recorded.
- [ ] Signoff reports archived privately.
- [ ] Tape-out data checksum/version recorded.
- [ ] Measurement plan prepared.
- [ ] Restricted foundry files are not copied into public repositories.
