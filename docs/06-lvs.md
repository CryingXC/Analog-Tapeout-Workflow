# 06 · LVS

Layout Versus Schematic checks whether the implemented layout corresponds to the intended electrical design.

## Think in three layers

1. **Ports / pins**
2. **Connectivity / nets**
3. **Devices / parameters**

A mismatch at a higher layer can create many downstream errors.

## Common root causes

- missing or renamed pins;
- power/ground naming mismatch;
- shorted or open nets;
- source/drain interpretation differences;
- device array/finger interpretation;
- hierarchy or black-box mismatch;
- wrong reference/source view.

## Sub-block pin mismatch

A common hierarchical failure occurs when a sub-layout is compared as a standalone cell but the corresponding schematic does not expose the same interface.

Possible solutions depend on intent: make the sub-block interface complete, use a wrapper that represents the intended boundary, or compare at the higher hierarchy where the missing connectivity is actually defined.

Do not “fix” LVS by deleting meaningful pins just to make the report green.

## Debug order

Start from top-level summary → ports → unmatched nets → unmatched devices. Fixing the first structural mismatch often collapses many secondary errors.
