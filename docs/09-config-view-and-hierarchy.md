# 09 · Config Views & Hierarchy

A configuration view is a controlled answer to:

> For each cell in this hierarchy, which implementation view should the simulator/netlister use?

## Typical mixed hierarchy

A post-layout top-level simulation may legitimately contain an extracted view for one completed block, schematic view for another, a behavioral model for an environment block, and ideal testbench sources.

## Why view order matters

If the view-search order prefers `schematic` before the intended extracted/calibre view, the simulator may silently use the pre-layout implementation.

Always inspect the resolved hierarchy rather than assuming the setup worked.

## Practical debugging

When a post-layout result looks suspiciously identical to pre-layout:

1. inspect the config hierarchy;
2. check the selected view for the critical cell;
3. inspect the generated netlist for extracted parasitics;
4. confirm the expected extracted cell/path is referenced.

This is more reliable than changing environment strings blindly.
