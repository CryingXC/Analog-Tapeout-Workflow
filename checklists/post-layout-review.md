# Post-Layout Review Checklist

- [ ] Confirm the extracted view exists and is current.
- [ ] Confirm the config resolves the intended cells to extracted/calibre views.
- [ ] Inspect the generated netlist for parasitic R/C elements.
- [ ] Re-run nominal DC operating point.
- [ ] Compare key pre-layout and post-layout metrics side-by-side.
- [ ] Re-run startup.
- [ ] Re-run the most stressful transient cases.
- [ ] Re-run critical PVT corners.
- [ ] Re-run stability/AC analysis where applicable.
- [ ] Check for new overshoot, ringing, delay, settling or current spikes.
- [ ] Identify whether degradation is dominated by R, C or coupling.
- [ ] Record extraction setup and view versions with the result.
