# 02 · Schematic & Pre-layout Verification

Pre-layout verification establishes whether the **intended circuit** is viable before parasitics and physical implementation are introduced.

## Recommended order

1. **DC operating point** — region of operation, headroom, bias-current sanity and device stress.
2. **Small-signal / loop checks** — gain, poles/zeros, phase margin, PSRR or output impedance when relevant.
3. **Transient** — startup, line/load steps, clocks/switching, enable/reset sequencing and recovery.
4. **Corners** — deterministic PVT first, statistical mismatch after nominal/corner behavior is understood.

## Hierarchy discipline

Keep block interfaces explicit. A clean hierarchy helps later when running sub-block LVS, swapping schematic/extracted views, isolating post-layout regressions and building a full-chip config.

## Save a golden pre-layout baseline

For each important metric, save the nominal value and testbench conditions. Post-layout verification is much easier when the comparison is “what changed and why?” rather than “does the new waveform look plausible?”
