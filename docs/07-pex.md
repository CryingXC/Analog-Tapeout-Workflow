# 07 · PEX

Parasitic extraction converts physical geometry into an electrically richer network.

## What appears after extraction

Depending on the setup, the extracted view may include wire resistance, device terminal resistance, ground capacitance, coupling capacitance and many internal RC nodes.

## Why the “big resistor/capacitor network” is normal

PEX is representing metal, contacts, vias and coupling as circuit elements. A dense block may produce a large network even when the original schematic is compact.

The right question is not “why are there so many resistors?” but:

> Which parasitic paths materially affect the metric I care about?

## Extraction choices

Extraction can vary by R-only/C-only/RC, coupling on/off, hierarchy preservation/flattening and other authorized settings. Use the extraction mode required by the verification goal and signoff flow.

## Keep provenance

Record which extraction setup produced a result. “Post-layout” without knowing the extraction assumptions is incomplete evidence.
