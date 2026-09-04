# 01 · Specification & Test Plan

Do not begin with transistor sizing. Begin with a measurable specification and a test plan.

## Convert product language into measurable quantities

| Product statement | Engineering metric |
|---|---|
| “stable output” | phase margin, settling, no sustained oscillation |
| “low power” | quiescent current, startup energy |
| “fast transient” | undershoot/overshoot, recovery time |
| “robust” | PVT pass rate, Monte Carlo yield proxy |
| “safe startup” | no overvoltage, no illegal device stress |

## Build the verification matrix early

A useful matrix includes supply range, temperature range, process corners, load conditions, startup sequences, AC/stability conditions, transient stimuli, statistical mismatch where relevant, and device-stress checks.

## Define extraction windows before simulation

For metrics such as average current, efficiency, ripple or settling, define the steady-state window, trigger thresholds, averaging method and sign convention before looking at the result.

This avoids “moving the window until the result looks good.”

## Tape-out implication

The final measurement plan should be traceable back to these same specifications. A metric that cannot be measured after fabrication deserves explicit justification.
