# Hobbies error-head intervention

This is a post hoc intervention on the already consumed development partition. The external confirmation and the consumed item holdout are not accessed. Two specialist error heads use the same 107,384 Hobbies rows from the original first-seed 600,000-row risk-training sample. One uses the original 21 features; the other adds eight observed-history features. The shared error head is retained as the baseline. The point forecast, censor adapter, demand head, and risk cap are unchanged.

For each 56-day and 112-day window ending at the forecast origin, the added features are the observed positive-day count, mean observed units on positive days, population squared coefficient of variation of positive observed units, and elapsed days since the last positive observation capped at the window length. Positive-size mean and CV squared are zero when there are no positive observations; recency is the window length. These quantities describe observed sales, not identified latent demand. The original features retain the benchmark's historical strict-censor indicators.

The score is the clipped predicted absolute error minus the cap times the clipped frozen demand prediction. A single largest common threshold must meet the WAPE cap and 35% row-coverage floor in both development calibration blocks A and B. It is then transferred unchanged to the later development block. The separately reported largest feasible prefix on each block uses that block's outcomes and is a ranking diagnostic, not a deployable policy. No specialist is selected on later-block performance.

The two heads use squared-error targets computed from pre-mechanical-censoring labels. This experiment does not solve the missing-label problem in natural stockouts. Category specialization changes the training population relative to the shared head; the comparison between the two specialists isolates the added features while holding the training rows fixed.

The runner reconstructs the original historical point forecasts and requires bitwise agreement with all three retained development blocks before fitting. Its frozen protocol records source/model/input hashes and the runtime. The original risk training feature arrays were not retained, so exact reconstruction is part of this experiment. The final verification also checks that the shared head reproduces the previously published Hobbies error MSE and bias in all three blocks. Large reconstructed caches are omitted from the distribution.

Verify the supplied aggregates without fitting:

```bash
python code/verify_hobbies_intervention.py --output reproduction_outputs/hobbies/AUDIT.json
```

To reconstruct from the permitted design inputs, use the runtime versions recorded in PROTOCOL.json and run `code/run_hobbies_intervention.py --data /path/to/design_inputs`. The runner verifies all input hashes and will reuse supplied specialist models. The directory must contain design_outcomes_v0_5.npz, calendar.csv, and sell_prices.csv. No other raw inputs are accepted.
