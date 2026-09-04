# 08 · Post-layout Simulation

Post-layout simulation asks whether the **implemented physical circuit** still meets the specification.

## First question: which view is actually simulated?

Verify the netlisted hierarchy. A simulation called “post-layout” is meaningless if the critical cells still resolve to schematic views.

## Compare against the golden pre-layout baseline

Track deltas in DC bias, gain/bandwidth/phase margin, startup, delay, rise/fall time, transient undershoot/overshoot, power/current and ripple/noise where relevant.

## Why post-layout can be much slower

PEX adds nodes and RC time constants. Switching circuits may also force the transient solver to resolve fast edges while integrating long startup windows.

Practical responses include checking whether the analysis window is necessary, avoiding unnecessarily strict tolerances, using a maxstep appropriate to the phenomenon, reducing unnecessary saved nodes, and debugging smaller hierarchy first.

Do not trade away correctness just to make the progress bar move.
