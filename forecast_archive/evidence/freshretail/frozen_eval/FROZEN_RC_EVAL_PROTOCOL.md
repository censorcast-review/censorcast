# Frozen protocol: FreshRetailNet natural-stockout evaluation

Frozen before any row-level access to the official FreshRetailNet `eval` split.

## Input and population

- Dataset: `Dingdong-Inc/FreshRetailNet-50K`, revision
  `08c1fab7f9257bc73679d415d65d644165d351d4`.
- Development input: the deterministic first 2,000 complete train series,
  cached as `freshretail_2000_train_only.pkl.gz` with SHA-256
  `5dc9bcca4b42f25784895ba6327a06412860571a2c63a1fd6e285d521771bed3`.
- Evaluation population: the same 2,000 store-product identities in the seven
  official future dates. The primary estimand uses only target rows with no
  recorded stockout hours, because recorded sales identify demand only there.
  All-row recorded-sales metrics are secondary and are not latent-demand
  claims.

## Frozen forecasting procedure

1. Construct direct horizons 1--7 from origin-available history and scheduled
   discount/holiday/activity covariates using the existing v0.3 feature builder.
2. Fit a target encoder on the early train block only.
3. Fit an XGBoost absolute-error base model only on uncensored early-block
   labels. Use seed 20260907, 600 boosting rounds, learning rate 0.03, depth 8,
   minimum child weight 80, row/column subsampling 0.9, L2 2.0, and histogram
   trees. Cap the sampled fit matrix at 600,000 rows.
4. Fit an XGBoost logistic stockout-risk head on all early-block rows with the
   same encoded predictors and seed.
5. Freeze CENSORCAST-RC at eight pooled risk-quantile bins, management-group
   conditioning, and log-scale shrinkage 0.75. Fit its cell multipliers by the
   weighted-median solution on all five fixed-origin train tail blocks.
6. Compare against the identical base model with management-group-only
   weighted-median scaling. No parameter, bin count, shrinkage, feature, or
   eligibility rule may change after eval access.

## Outcomes and inference

- Primary: WAPE difference, RC minus scaled base, on fully available eval rows.
- Secondary: MAE, RMSE, signed percentage bias, all-row recorded-sales WAPE,
  and results split by management group and forecast horizon.
- Inference: paired cluster bootstrap over store-product series, 4,000 draws,
  seed 20260907. Report the two-sided percentile 95% interval.
- The eval split is opened once. There is no refit, reselection, or threshold
  search after scoring. A null or adverse result is retained.

## Interpretation boundary

This experiment tests transfer to a stockout-annotated natural retail panel.
It does not observe latent demand on stockout rows, so it cannot validate
hidden-demand recovery there. It tests whether a calibration learned from
availability-identifiable train targets improves future demand forecasts on
availability-identifiable eval targets.
