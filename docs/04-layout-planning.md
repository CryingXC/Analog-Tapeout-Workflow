# 04 · Layout Planning

Layout is circuit design in geometry.

## Before drawing polygons

Decide the floorplan, supply/ground strategy, sensitive-node locations, matching groups, high-current routes, clock/switching routes, substrate/guard strategy, and hierarchy pin locations.

## Matching

For matched devices, consider common orientation, proximity, symmetric routing, dummy devices where appropriate, and common-centroid/interdigitation when gradients matter.

The exact technique depends on device type and mismatch mechanism; there is no universal “common centroid = always better” rule.

## Parasitic-aware routing

Ask which nets are sensitive to series resistance, load capacitance, coupling, current density and switching-edge injection.

A net that is harmless in the schematic can dominate the post-layout result if it becomes long, resistive or strongly coupled.

## Pin/interface discipline

Pin names, directions and hierarchy must remain consistent with the schematic intent. Many LVS problems are interface problems disguised as device mismatches.
