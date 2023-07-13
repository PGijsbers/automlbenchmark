

### Constraints definition

Now that we have defined a list of datasets, we also need to enforce some constraints on the autoML training.

Default constraint definitions are available in `resources/constraint.yaml`. When no constraint is specified at the command line, the `test` constraint definition is used by default.

THe application supports the following constraints:
- `folds` (default=10): tell the number of tasks that will be created by default for each dataset of the benchmark. For example, if all datasets support 10 folds, setting a constraint `folds: 2` will create a task only for the first 2 folds by default.
- `max_runtime_seconds` (default=3600): maximum time assigned for each individual benchmark task. This parameter is usually passed directly to the framework: if it doesn't respect the constraint, the application will abort the task after `2 * max_runtime_seconds`. In any case, the real task running time is always available in the results.
- `cores` (default=-1): amount of cores used for each automl task. If <= 0, it will try to use all cores.
- `max_mem_size_mb` (default=-1): amount of memory assigned to each automl task. If <= 0, then the amount of memory is computed from os available memory.
- `min_vol_size_mb` (default=-1): minimum amount of free space required on the volume. If <= 0, skips verification. If the requirement is not fulfilled, a warning message will be printed, but the task will still be attempted.

_Example:_

Following the [custom configuration](#custom-configuration), it is possible to override and/or add constraints by creating the following `constraints.yaml` file in your `user_dir`:

```yaml
---

test:
  folds: 1
  max_runtime_seconds: 120

1h16c:
  folds: 10
  max_runtime_seconds: 3600
  cores: 16

1h32c:
  folds: 10
  max_runtime_seconds: 3600
  cores: 32

4h16c:
  folds: 10
  max_runtime_seconds: 14400
  cores: 16
  min_vol_size_mb: 65536

8h16c:
  folds: 10
  max_runtime_seconds: 28800
  cores: 16
  min_vol_size_mb: 65536

```

The new constraints can now be passed on the command line when executing the benchmark:
```bash
python runbenchmark.py randomforest validation 1h16c
```