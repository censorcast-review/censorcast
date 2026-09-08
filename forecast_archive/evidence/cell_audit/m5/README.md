# M5 cell-comparator audit and a fixed multiplier floor

This additive audit preserves all original inputs and evidence. It does not
open a new holdout or choose a method from Later outcomes.

## Comparator correction

The original cell-table routine computed its `base_wape` from the **raw**
hierarchy forecast, whereas the main comparator includes the fitted category
scale. The same routine correctly computed RC by multiplying the raw forecast
by the saved absolute cell scale. This is a definition mismatch, not a different
model: the primary hierarchy model SHA-256 is
`2527c577cb863cbb72c3af6c78509b179aa70543ea5c170f6564449541d34c90`.

The relevant original source is
`code/risk_calibration/run_attribution_and_integration_controls.py`:
`cell_rows` (lines 105–142), especially lines 125 and 139, and its calls with
`base_valid` / `base_later`. Earlier cell checks covered populations and target
mass but did not compare the cell Base error mass to the main comparator.

`RESULTS.json` and `cells.csv` retain four explicit definitions: `raw`,
`base` (category-scaled), `rc`, and `floor_0_5`. In the corrected table, Base is
always `base`; RC is unchanged apart from insignificant scalar float32 versus
vector float64 multiplication roundoff. The new audit checks each population's
cell error masses against independently scored category and pooled totals.

## One fixed floor

The existing cell multiplier is absolute: it multiplies the raw hierarchy
forecast. The diagnostic applies `max(saved_multiplier, 0.5) * raw_forecast`.
It does **not** multiply the category-scaled baseline by this number, refit
forecast/risk heads, search a floor grid, or change the primary method.

`PROTOCOL.json` was written before full-validation/Later replay. Full-validation
loss uses the final refitted scales and is explicitly in-sample. Its predictions
and those on Later were replayed from the archived models.

`AMENDMENT_SPLIT.json` was written before the separate held-out time-half
calibration diagnostic. A single fixed 8-bin, 0.75-shrinkage calibration is fitted
on validation days through 1373, including its category scales and pooled bin
edges. Days 1374–1433 are scored without refitting. `SPLIT_POLICY.json` contains
that policy and `SPLIT_RESULTS.json` all four metrics and error masses. The
unfloored split result exactly reproduces the archived selection-period
metrics, validating the reconstructed scale-fitting routine.

All these dates were previously consumed during development. The held-out-half
designation describes this fixed calibration split, not independent confirmation
or a new selection exercise. The original full-validation policy is retained
for Later.

## Main findings

- Correct pooled Later Base/RC WAPE: 0.6713924902 / 0.6685093103.
- Foods bin 8: Base 0.5934940627, RC 0.5872381909. Its reduction is
  6,076.95 absolute-error units, 72.25% of the net 8,411.39-unit reduction.
- Hobbies bin 3 adds 392.91 error units; Hobbies bin 8 saves only 39.69.
- Four near-zero-multiplier cells cover 14.115% of rows and 1.393% of target
  mass. Only 4,031 of their 294,310 rows had a positive raw forecast. It would
  therefore be incorrect to describe all 14.115% as newly zeroed forecasts.
- The 0.5 floor worsens held-out-half pooled WAPE from 0.7008797248 to
  0.7012449167, while improving Later from 0.6685093103 to 0.6684224867.
  This reversal is not used to replace the primary method.
- Hobbies Later WAPE becomes 0.8569889888, mitigating but not eliminating its
  deterioration relative to Base 0.8568664854. The original RC value was
  0.8579591316.

`RECEIPT.json`: 268 checks pass. `SPLIT_RESULTS.json`: 16 checks pass.

## Reproduction

Use the decoded M5 development inputs from the saved-model replay; write to a
new output directory to preserve these receipts. Run
`code/analyze_m5_cells_floor.py` with `--package`, `--inputs`, and `--output`.
For the split diagnostic, copy the documented fixed amendment to that new
audit directory and run `code/analyze_m5_floor_split.py` with `--package`,
`--inputs`, and `--audit`. Both scripts support `--tables-only` to regenerate
LaTeX from the stored results without inference or fitting.
