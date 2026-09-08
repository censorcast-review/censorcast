# CENSORCAST v0.5: independent M5 protocol

## 1. Status and scientific boundary

v0.5 is a new study, not a continuation or rescue analysis of the failed v0.4
FreshRetailNet guardian.  The v0.4 guardian, its row-level outcomes, and the
FreshRetailNet eval/test split are prohibited inputs.  Its spent alpha is not
recycled.  v0.5 begins with a new data source, item-cluster partition, access
ledger, policy freeze, single-use guardian and alpha budget.

The new source is the M5 Forecasting Accuracy data fixed at Zenodo record
`10203108` (DOI `10.5281/zenodo.10203108`).  The source checksums in
`configs/PROTOCOL_v0_5.json` are binding.

## 2. Claim limitation

M5 records unit sales but not latent demand lost to real stockouts.  Therefore
v0.5 does **not** claim identification of natural stockouts.  Its primary
estimand is recovery of known unit demand after a prespecified, prequential
inventory-cap mechanism mechanically hides part of that demand.  A later
real-world claim would require a separate dataset with observed inventory or a
credible latent-demand benchmark.

## 3. Independent item-cluster split

All 3,049 `item_id` values are ordered by
`SHA256(salt || NUL || item_id)` before any outcome summary is computed.

| Role | Items | Bottom series | Statistical use |
|---|---:|---:|---|
| design | 1,829 | 18,290 | model, score and policy development |
| fresh guardian | 610 | 6,100 | one confirmatory use after freeze |
| external | 610 | 6,100 | final evaluation only after certificate |

An item and all ten of its store series belong to exactly one role.  This tests
generalization to products absent from development rather than merely to new
rows of a familiar product.

## 4. Time topology

The 1,941 days are fixed before analysis:

| Block | Days | Use |
|---|---:|---|
| fit | 1–1,313 | base forecasting models |
| selection | 1,314–1,433 | baseline and architecture selection |
| risk_train | 1,434–1,553 | cross-fitted risk layer |
| calibration A | 1,554–1,673 | policy calibration block 1 |
| calibration B | 1,674–1,793 | policy calibration block 2 |
| shadow | 1,794–1,913 | untouched development confirmation |
| external final | 1,914–1,941 | sealed final 28-day horizon |

Forecasts use horizons 1–7 and only information available at each rolling
origin.  The final 28 days remain sealed through development and guardian use.

## 5. Controlled censoring

For each series, days 1–56 are an uncensored warmup.  Thereafter:

1. `level_t = 0.90 level_(t-1) + 0.10 observed_(t-1)`;
2. `capacity_t = max(1, ceil(1.15 level_t + 0.25 sqrt(level_t + 1)))`;
3. `observed_t = min(true_t, capacity_t)`;
4. `censored_t = true_t > capacity_t`.

The mechanism never uses the current or future outcome to set capacity.  Its
parameters are not tuned after seeing M5 outcomes.  A design-only validity gate
requires a row censoring rate in `[0.005, 0.35]` and hidden-demand mass in
`[0.002, 0.40]`.  Failure stops model development; it does not authorize a
post-hoc change to the mechanism.

## 6. Forecast and risk-layer development

The point proposal is compared with the strongest frozen non-censor-aware
baseline.  The v0.5 risk layer must be trained prequentially and cross-fitted.
Its allowed features are strictly prior residual history, forecast-ensemble
dispersion, intermittent-demand statistics, price/event regime variables and
distance from design support.  Current or future realized error is forbidden.

Every unique deployable score threshold is evaluated.  Before any guardian
opening, the same threshold must survive calibration A, calibration B, shadow
and prespecified category strata with margin-adjusted cluster-bootstrap bounds.

## 7. Contracts

The primary contract is task-relative and fixed by rule:

- accepted WAPE no greater than `0.90 ×` the frozen full-coverage baseline WAPE
  on selection;
- accepted-row coverage at least `0.30`.

The stricter development reachability margin is a WAPE-ratio UCB no greater
than `0.85` and a coverage LCB of at least `0.35`.  The legacy absolute contract
of WAPE `0.30` at coverage `0.30` is reported only as a diagnostic.

## 8. Confirmatory sequence

If and only if design development passes and the policy is administratively
frozen, the 610-item guardian may be opened once.  The familywise alpha is
`0.05`.  Six one-sided endpoints—coverage and accepted-WAPE ratio in each of
three blocks—use Holm step-down adjustment with `item_id` cluster resampling.
All six must pass for a certificate.

The external item group and days 1,914–1,941 may be opened only after a separate
audit confirms the guardian certificate.  A failed guardian ends that protocol;
it cannot be used to retune the score or threshold.

## 9. Preparation boundary

The preparation program may copy and mechanically shard bytes without showing
guardian/external summaries.  It performs zero training and zero policy
selection.  It reports censoring diagnostics only for design items, deletes the
temporary plaintext raw sales copy after verified sharding, hashes every shard,
and initializes both sealed-use counters at zero.

