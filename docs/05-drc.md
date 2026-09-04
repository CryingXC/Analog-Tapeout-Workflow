# 05 · DRC

Design Rule Check answers a geometric question:

> Does this physical layout obey the manufacturing rules for the selected process?

## Good DRC workflow

1. Run early on small blocks.
2. Classify violations by root cause, not only by count.
3. Fix repeated-rule patterns systematically.
4. Re-run after hierarchy/top-level assembly.
5. Perform the required final signoff run using the authorized rule deck.

## What DRC does not prove

A DRC-clean layout can still have wrong connectivity, missing/extra devices, swapped pins, poor matching, unstable analog behavior or unacceptable parasitics.

That is why DRC must be paired with LVS, PEX and simulation.

## Public repository rule

Never publish the foundry rule deck to “show how DRC works.” Explain the methodology; keep the actual deck in the authorized environment.
