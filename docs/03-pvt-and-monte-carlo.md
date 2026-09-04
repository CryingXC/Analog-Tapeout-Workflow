# 03 · PVT & Monte Carlo

PVT corners and Monte Carlo answer different questions.

## PVT: deterministic extremes

PVT asks whether the design works across process, supply and temperature combinations. It exposes deterministic sensitivity such as reduced gain, timing shifts, weaker drive, leakage increase or startup failure.

## Monte Carlo: distributions

Monte Carlo asks how random variation changes a metric distribution. Typical targets include offset, bias/reference spread, gain spread, mirror mismatch and comparator decision variation.

## Common mistake

Do not use Monte Carlo as a substitute for understanding nominal and corner failures. A statistical histogram cannot rescue a design that already fails a deterministic corner.

## Result format

| Metric | Nominal | Worst PVT | Monte Carlo summary | Requirement |
|---|---:|---:|---:|---:|

The important output is **margin**, not the number of simulations launched.
