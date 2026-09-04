# 11 · Packaging, PCB & Measurement

A fabricated die is not yet a measured circuit.

## Packaging adds electrical elements

Bond wires and package structures contribute parasitic R/L/C. Supply impedance and high-speed edges may therefore differ from ideal simulation.

## PCB bring-up strategy

1. Inspect assembly and orientation.
2. Check shorts between supplies and ground before power.
3. Use current-limited supplies.
4. Power rails in the intended sequence.
5. Confirm static current and DC outputs first.
6. Only then apply clocks, load steps or high-speed stimuli.
7. Record instrument settings and probe points.

## Measurement correlation

When silicon differs from simulation, separate the possible layers: circuit/model mismatch, package parasitics, PCB/loading, instrument bandwidth, probe/grounding, assembly issue and incorrect stimulus or measurement point.

The goal is not to prove the simulation “right.” The goal is to explain the physical system.
