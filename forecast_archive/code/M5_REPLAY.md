# Independent M5 replay and fixed-condition artifact recovery

The original source snapshot contains imports of two helper modules that were
not included in its archive. It also retains paths to an older package layout.
The new scripts in this directory provide an additive execution path without
editing the historical source or evidence.

## Replay the saved primary experiments

From the package root, use a new output directory outside the package:

```bash
python code/replay_m5.py --output /tmp/censorcast_m5_replay --threads 4
```

This reads the bundled M5 development ZIP, three saved hierarchy base models,
three saved hit-risk models, and saved calibration policies. It performs no
training, calibration fitting, policy selection, or new holdout access. The
default run covers all three seeds and all three previously used M5 blocks.
For a smaller run, append `--seeds 20260906 --blocks shadow`.

The independent replay checks:

- primary validation predictions against the saved prediction array;
- validation risk quantiles and calibration-cell row counts and demand mass;
- base and RC metrics for each requested seed and block;
- item identities, demand mass, base error, and RC error against saved item
  sufficient statistics;
- all five matched-score controls using their saved policies on Later.

Outputs are `REPLAY_RESULTS.json`, `REPLAY_RECEIPT.json`, and per-item NPZ files.
An incomplete or mismatching replay does not earn a PASS: the receipt records
each comparison, its numerical tolerance, and any failed checks.

The seven hierarchy feature formulas are transcribed from the bundled
`risk_calibration/run_hierarchy_pilot.py`. Policy application and hit prediction
are independent reconstructions of documented operations. Numerical agreement
for the archived inputs does not establish source identity with the omitted
helpers or behavior on all possible inputs.

## Refit the two controls with omitted model files

The earlier archive included q-as-feature and truth-label control metrics and
declared model hashes, but omitted the corresponding `.ubj` models. The reason
for that omission is not documented. The saved JSON values alone cannot support
an independent model replay of those two controls.

After the primary replay, run:

```bash
python code/reproduce_m5_missing_controls.py \
  --input-dir /tmp/censorcast_m5_replay/extracted_inputs \
  --output /tmp/censorcast_m5_control_refit
```

This is a **new exploratory fixed-condition reproduction**, not restoration of
the original preregistration. It records a new protocol and code/input hashes
before the new fits, uses the archived 1.2-million-row sampling rule and seed,
and executes both fixed 750-round models without outcome-dependent selection.
It saves both model files, validation and Later predictions, item sufficient
statistics, paired item bootstrap intervals, and differences from the earlier
reported values. Exact model hash agreement, when achieved, is reported
separately from metric agreement. The old frozen files remain unchanged.

Both scripts need NumPy, pandas, XGBoost 2.1.4, and LightGBM 4.6.0. The package
requirements record the reference runtime versions. The replay extracts about
267 MB of data/cache files; the full feature panel also needs several GB of RAM.
