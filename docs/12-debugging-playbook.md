# 12 · Debugging Playbook

| Symptom | First things to check |
|---|---|
| LVS reports missing pins | schematic/layout interface, pin names, hierarchy boundary |
| LVS has many unmatched devices | fix ports/nets first; verify reference view and source setup |
| PEX result shows a huge RC network | expected extraction detail; inspect extraction mode and hierarchy |
| Post-layout sim is extremely slow | extracted node count, long time window, fast edges, saved nodes, solver timestep |
| Post-layout result is identical to pre-layout | config/view resolution, generated netlist, extracted view actually selected |
| Post-layout waveform shifts badly | parasitic loading, series resistance, coupling, bias-node sensitivity |
| Simulation does not start cleanty | initial conditions, startup sequencing, reset/enable state, floating nodes |
| Full-chip passes but sub-block LVS fails | standalone sub-block may have incomplete interface; compare hierarchy assumptions |
| One corner fails only | identify the physical sensitivity: gain, timing, leakage, drive, headroom or startup |
| Measurement disagrees with simulation | package, PCB, loading, probing, instrument setup, silicon/model variation |

## Debugging principle

Reduce the problem until one hypothesis can be falsified.

Bad debugging: change several tolerances, delays and view settings at once.

Good debugging: verify one view, one hierarchy boundary, one metric and one stimulus at a time.
