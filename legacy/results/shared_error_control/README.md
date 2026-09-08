# Shared error-head feature control

This development-only matched control adds eight intermittency summaries to the original global 600,000-row error-head fit. It preserves the original row sample, point forecast, demand head, target, tree capacity and calibration rule. The prior three Hobbies intervention records are retained unchanged.

Published verification, without fitting or raw data:

```sh
python code/verify_shared_error_intervention.py
```

The audit is written to `reproduction_outputs/shared_error_control/AUDIT.json`, outside archived evidence. Optional `--arrays` verifies retained development caches when available; caches are not included in the public package.

`PROTOCOL.json` was frozen before reconstruction and fitting. `SELECTED_POLICY.json` records A/B selection before later-block metrics. `RESULTS.json`, `models/`, and `AUDIT.json` retain the completed fit and verification evidence. Prior cache hashes document reconstruction provenance even when the underlying caches are excluded from the public artifact.
