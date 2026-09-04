# Measurement Bring-up Checklist

## Before power
- [ ] Package orientation verified.
- [ ] PCB assembly visually inspected.
- [ ] Supply-to-ground resistance checked for obvious shorts.
- [ ] Instrument voltage/current limits configured.
- [ ] Pin map cross-checked with package/bond map.

## First power
- [ ] Use current-limited supply.
- [ ] Apply intended power sequence.
- [ ] Monitor supply current continuously.
- [ ] Verify reference/bias/DC output before dynamic tests.

## Functional tests
- [ ] Enable/reset controls verified.
- [ ] Static load points measured.
- [ ] Line/load transient tests performed.
- [ ] AC/PSRR/stability-related tests performed if instrumentation permits.
- [ ] Instrument bandwidth/probe loading documented.

## Correlation
- [ ] Measurement conditions match the simulation case.
- [ ] Package/PCB parasitics considered.
- [ ] Deviations logged before changing the test setup.
- [ ] Failed hardware is preserved for root-cause analysis.
