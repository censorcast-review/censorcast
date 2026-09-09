# Evidence boundaries and next empirical questions

This note records interpretation changes and unexecuted study designs. It is not a preregistration or a report of new experiments.

## Corrections grounded in existing results

- The original external protocol has 48 endpoints: 24 risk upper bounds fail and 24 case-coverage lower bounds pass. It does not contain 48 failed risk bounds. Pooled point risk passes; Hobbies and Household point risks fail.
- Six selected policies under the stricter A design have pointwise 95% evaluation risk upper bounds below the reporting cap. This is approximate, conditional evidence, not a simultaneous population guarantee. All ten A-feasible candidates passed B; a causal benefit of the screen is not isolated.
- At cap 0.68, the residual predictor has no coverage contrast, while L1 and Chronos retain exposure differences of 0.83 and 2.93 points. At 0.70 all three have zero contrast. Cap sensitivity limits generalization; the reporting cap has no claimed universal operational justification.
- Original non-retail intervals adjust four endpoints (98.75%). The later menu comparison adjusts eight (99.375%) and uses its declared seed. They reuse data, not independent confirmations.
- Delicious is calibration-infeasible under the primary cap and case floor, rather than unexplained. Yeast does not establish a useful learned-policy reversal.

## Changes made in the manuscript

The abstract now reports both sides of the exchange: retail demand coverage increases 7.64--10.63 points while case coverage decreases 35.18--40.66 points. Bike exchanges 13.34 case points for 5.01 exposure points. The exchange is valuable only relative to a specified utility. The abstract leads with budget auditing, supported by the quantitative theory. The main text defines Later, distinguishes interval families, and states the predictor-specific cap sensitivity.

## Remaining experiment: no artificial censoring

The bundled M5 development input archive contains truth, observed, capacity, metadata, calendar, and prices. Inputs needed for a paired development experiment are present. No new fit was performed for this revision.

A valid comparison must reconstruct lag, rolling, and hierarchy features from complete recorded sales in the no-artificial-censoring arm, and refit the predictor and both selector heads. Reusing forecasts trained on censored history is not an uncensored control. Fix identical series, dates, sampled rows, model budgets, and candidate menus across arms; exclude capacity/fill/hit features from both arms for the primary matched-feature comparison. Report absolute and calibration-normalized cap grids, all infeasible conditions, full-coverage risk, both selected coverages, and budget decomposition. Keep the original information-rich arm as a separate secondary comparison. No artificial censoring does not establish that recorded M5 sales equal latent customer demand. Existing development outcomes remain retrospective.

## Remaining experiment: estimated-head diagnosis

Neither observed Y nor realized absolute error is the conditional moment w(X) or ell(X). Replacing fitted heads with those labels is an ex-post information diagnostic, not a conditional-information oracle and not an implementable selector. A real-data study should compare forward-time error-head and exposure-head estimation variants in a factorial design, keeping the point predictor fixed and choosing configurations only on calibration. Report held-out head losses, decision-boundary errors, feasibility, and coverage, without claiming causal attribution to a single head from loss alone. A complementary simulation with analytically known conditional moments can isolate controlled perturbations of each head; its conclusions are simulation-specific.

## Remaining methodological boundary

The present work is an audit of selective policies, not a new distribution-free risk-control method. A valid finite-family test requires a justified sampling model and suitable tail or boundedness assumptions. A finite observed maximum is not a population bound. Relabeling the cluster-bootstrap screen as LTT or conformal risk control would not supply those assumptions. A future independent confirmation must lock the utility, candidate family, risk procedure, and multiplicity before accessing new outcomes.
