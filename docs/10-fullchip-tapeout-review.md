# 10 · Full-chip & Tape-out Review

Before release, review the chip as a system.

## Electrical

- supplies and grounds;
- enable/reset/default states;
- analog/digital interface polarity;
- bias/reference distribution;
- top-level pin mapping;
- startup and power sequencing;
- device-stress conditions.

## Physical

- final DRC;
- final LVS;
- required extraction/signoff;
- pad-ring/top-level connectivity;
- bond-pad naming and mapping;
- hierarchy consistency.

## Verification evidence

Keep the nominal baseline, PVT summary, Monte Carlo summary where applicable, post-layout deltas, known limitations and risk list.

## Release discipline

Freeze the design version, layout version, netlist/config version, signoff reports, test plan and package/pin map.

A tape-out review should make it difficult to accidentally submit “the wrong but almost identical version.”
