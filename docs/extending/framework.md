# Adding an AutoML Framework

## Using a Different Hyperparameter Configuration

When you want to use an existing framework integration with a different hyperparameter
configuration, it is often enough to write only a custom framework definition without
further changes. 

Framework definitions accept a `params` dictionary for pass-through parameters, 
i.e., parameters that are directly accessible from the `exec.py` file in the framework 
integration executing the AutoML training. *Most* integration scripts use this to
overwrite any (default) hyperparameter value. Use the `extends` field to indicate
which framework definition to copy default values from, and then add any fields to
overwrite. In the example below the `n_estimators` and `verbose` params are passed 
directly to the `RandomForestClassifier`, which will now train only 200 trees
(default is 2000):

```yaml
RandomForest_custom:
  extends: RandomForest
  params:
    n_estimators: 200
    verbose: true
```

This new definition can be used as normal: 
```
python runbenchmark.py randomforest_custom ...
```

!!! note
    By convention, param names starting with `_` are filtered out (they are not passed 
    to the framework) but are used for custom logic in the `exec.py`. For example, the
    `_save_artifact` field is often used to allow additional artifacts, such as logs or
    models, to be saved.
