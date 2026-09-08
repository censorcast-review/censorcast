# CENSORCAST v0.5 M5 design-development protocol

## Scientific question

Under mechanically imposed, prequential demand censoring, can a forecasting
system recover hidden unit demand more accurately than the strongest frozen
non-censor-aware baseline, and can it identify a useful subset whose aggregate
latent-demand WAPE stays below a baseline-relative contract?

## Data boundary

Only the 1,829-item design cluster and days 1–1913 may be read.  The fresh
guardian (610 disjoint items) and external split (610 further disjoint items)
remain sealed.  Shared calendar and price covariates are allowed because they
contain no latent-demand outcomes.  Item identity itself is excluded from the
model so the learned rule must transfer to unseen products.

## Forecast topology

The system issues one seven-day vector each week.  Every target day appears
once, at horizon 1–7, and every feature is computed at the associated origin.
The base models use fit-period targets only.  Selection chooses the strongest
baseline and the censor-aware adapter.  Risk-train fits the error model;
calibration A/B choose the risk-score family and exact threshold; shadow is
used once after that choice is fixed.

## Forecast models

The baseline family consists of lag-7 seasonal naive, four-week seasonal
median, and pooled Poisson HistGradientBoosting trained on observed sales while
ignoring capacity/censoring indicators.  The expert uses the same deployable
features but replaces censored training labels with the Poisson conditional
mean above the observed capacity, iterating three times.  A frozen classifier
estimates future censoring risk.  Selection chooses a nonnegative gated
correction from baseline toward the EM expert; strength zero remains an
explicit fallback.

## Risk layer

The instantaneous model predicts an upper quantile of absolute latent-demand
error from ensemble disagreement, censoring pressure, intermittency,
price/event regime, horizon, and support distance.  A strictly prior history
feature uses residuals against *observed* sales, not latent truth, so it is
available on unseen products.  Five predeclared mixtures of instantaneous and
historical error are compared.  Lower predicted excess error is safer.

## Contracts and bounds

Let B be the strongest baseline's full-coverage WAPE on selection.  Deployment
requires accepted WAPE no greater than 0.90B at coverage at least 0.30.
Development deliberately requires margin: a one-sided WAPE-ratio UCB no greater
than 0.85 and a coverage LCB at least 0.35.  Every unique deployable-score
threshold is examined on calibration A/B using item-cluster delta-method
bounds.  The chosen fixed policy is then checked with Bonferroni-adjusted
item-cluster bootstrap bounds on calibration A, calibration B, shadow, and
pooled product-category strata.

## Interpretation

All outcomes here are development evidence.  A GO authorizes only an
administrative freeze.  Statistical certification requires one later use of
the disjoint fresh guardian under its own alpha ledger.  The external split can
be opened only after that guardian certificate.
