

## Add a benchmark

In this section, `benchmark` means a suite of datasets that can be used to feed any of the available frameworks, in combination with a set of constraints (time limit, cpus, memory) enforced by the application.

A benchmark definition will then consist in a [datasets definition](#datasets-definition) and a [constraints definition](#constraint-definition).

Each dataset must contain a training set and a test set. There can be multiple training/test splits, in which case each split is named a `fold`, so that the same dataset can be benchmarked multiple times using a different fold.

### Datasets definition

A dataset definition consists in a `yaml` file listing all the task/datasets that will be used for the complete benchmark, 
or as an OpenML suite.

Default dataset definitions are available under folder `resources/benchmarks`.

Each task/dataset must have a `name` that should be unique (ignoring case) in the given definition file, it will also be used as an identifier, for example in the results.

This `name` can also be used on the command line (`-t` or `--task` argument) when we just want to execute a subset of the benchmark, often in combination with a specific fold (`-f` or `--fold` argument):
```bash
python runbenchmark.py randomforest validation -t bioresponse
python runbenchmark.py randomforest validation -t bioresponse eucalyptus
python runbenchmark.py randomforest validation -t bioresponse -f 0
python runbenchmark.py randomforest validation -t bioresponse eucalyptus -f 0 1 2
``` 

_Example:_

Following the [custom configuration](#custom-configuration), it is possible to override and/or add custom benchmark definitions by creating for example a `mybenchmark.yaml` file in your `user_dir/benchmarks`.

The benchmark can then be tested and then executed using the `1h4c` constraint:
```bash
python runbenchmark.py randomforest mybenchmark
python runbenchmark.py randomforest mybenchmark 1h4c
```


#### OpenML datasets

[OpenML] datasets are verified and annotated datasets, making them easy to consume.
However, the application doesn't directly consume those datasets today as the split between training data and test data is not immediately available.
For this we use [OpenML] tasks.

#### OpenML tasks

[OpenML] tasks provide ready to use datasets, usually split in 10-folds: for each fold, we have 1 training set and a test set.

The automlbenchmark application can directly consume those tasks using the following definition:
```yaml
- name: bioresponse
  openml_task_id: 9910
```
where `openml_task_id` allows accessing the OpenML task at `https://www.openml.org/t/{openml_task_id}` (in this example: <https://www.openml.org/t/9910>). 

Alternatively, you can run the benchmark on a single OpenML task without writing a benchmark definition:
```bash
python runbenchmark.py randomforest openml/t/59
```

#### File datasets

It is also possible to benchmark your own datasets, as soon as they follow some requirements:
- The data files should be in one of the currently supported format: [ARFF], [CSV] (ideally with header).
- Each dataset must contain at least one file for training data and one file for test data.
- If the dataset is represented as an archive (.zip, .tar, .tgz, .tbz) or a directory, then the data files must follow this naming convention to be detected correctly:
  - if there's only one file for training and one for test, they should be named `{name}_train.csv` and `{name}_test.csv` (in case of CSV files).
  - if there are multiple `folds`, they should follow a similar convention: `{name}_train_0.csv`, `{name}_test_0.csv``, {name}_train_1.csv`, `{name}_test_1.csv`, ...

_Example:_

Then the datasets can be declared in the benchmark definition file as follow:
```yaml
---

- name: example_csv
  dataset:
    train: /path/to/data/ExampleTraining.csv
    test:  /path/to/data/ExampleTest.csv
    target: TargetColumn
  folds: 1

- name: example_multi_folds
  dataset:
    train: 
      - /path/to/data/ExampleTraining_0.csv
      - /path/to/data/ExampleTraining_1.csv
    test:  
      - /path/to/data/ExampleTest_0.csv
      - /path/to/data/ExampleTest_1.csv
    target: TargetColumn
  folds: 2

- name: example_dir   # let's assume that the data folder contains 2 files: example_train.arff and example_test.arff
  dataset: 
    path: /path/to/data
    target: TargetColumn
  folds: 1

- name: example_dir_multi_folds   # let's assume that the data folder contains 6 files: example_train_0.arff, ..., example_train_2.arff, example_test_0.arff, ...
  dataset: 
    path: /path/to/data
    target: TargetColumn
  folds: 3

- name: example_archive  # let's assume that archive contains the same files as for example_dir_multi_folds
  dataset:
    path: /path/to/archive.zip
    target: TargetColumn
  folds: 3

- name: example_csv_http
  dataset:
    train: https://my.domain.org/data/ExampleTraining.csv
    test:  https://my.domain.org/data/ExampleTest.csv
    target: TargetColumn
  folds: 1

- name: example_archive_http
  dataset:
    path: https://my.domain.org/data/archive.tgz
    target: TargetColumn
  folds: 3

- name: example_autodetect
  dataset: /path/to/data/folder

- name: example_relative_to_input_dir
  dataset: "{input}/data/folder"

- name: example_relative_to_user_dir
  dataset:
    train: "{user}/data/train.csv"
    test: "{user}/data/test.csv"

```
**Note**:
- the naming convention is required only when `path` is pointing to a directory or an archive. If the files are listed explicitly, there's no constraint on the file names.
- the `target` attribute is optional but recommended, otherwise the application will try to autodetect the target:
  0. looking for a column named `target` or `class`.
  0. using the last column as a fallback.
- the `folds` attribute is also optional but recommended for those datasets as the default value is `folds=10` (default amount of folds in openml datasets), so if you don't have that many folds for your custom datasets, it is better to declare it explicitly here.
- Remote files are downloaded to the `input_dir` folder and archives are decompressed there as well, so you may want to change the value of this folder in your [custom config.yaml file](#custom-configuration) or specify it at the command line with the `-i` or `--indir` argument (by default, it points to the `~/.openml/cache` folder).

#### OpenML suites

[OpenML] suites are a collection of OpenML tasks, for example <https://www.openml.org/s/218>.
You can run the benchmark on an openml suite directly, without defining the benchmark in a local file:
```bash
python runbenchmark.py randomforest openml/s/218
```

You can define a new OpenML suite yourself, for example through the Python API.
[This openml-python tutorial](https://openml.github.io/openml-python/master/examples/30_extended/suites_tutorial.html#sphx-glr-examples-30-extended-suites-tutorial-py)
explains how to build your own suite.
An advantage of using an OpenML suite is that sharing it is easy as the suite and its datasets can be accessed through APIs in many programming languages.
