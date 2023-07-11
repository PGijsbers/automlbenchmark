---
title: Getting Started
description: Hello
---
# Getting Started

The AutoML Benchmark is a tool for benchmarking AutoML frameworks on tabular data.
It automates the installation of AutoML frameworks, passing it data, and evaluating
their predictions. 
[Our paper](https://arxiv.org/pdf/2207.12560.pdf) describes the design and showcases 
results from an evaluation using the benchmark. 
This guide goes over the minimum steps needed to evaluate an
AutoML framework on a toy dataset.

## Installation
These instructions assume that [Python 3.9 (or higher)](https://www.python.org/downloads/) 
and [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) are installed,
and are available under the alias `python` and `git`, respectively. We recommend
[Pyenv](https://github.com/pyenv/pyenv) for managing multiple Python installations,
if applicable.

First, clone the repository:

=== ":simple-linux::material-apple: UNIX"

    ```bash
    git clone https://github.com/openml/automlbenchmark.git --branch stable --depth 1
    cd automlbenchmark
    ```

=== ":simple-windows: Windows"

    ```bash
    git clone https://github.com/openml/automlbenchmark.git --branch stable --depth 1
    cd automlbenchmark
    ```

Create a virtual environments to install the dependencies in:

=== ":simple-linux::material-apple: UNIX"

    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

=== ":simple-windows: Windows"

    ```bash
    python -m venv ./venv
    venv/Scripts/activate
    ```

Then install the dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```


??? windows "Note for Windows users"

    The automated installation of AutoML frameworks is done using shell script,
    which doesn't work on Windows. We recommend you use
    [Docker](https://docs.docker.com/desktop/install/windows-install/) to run the
    examples below. First, install and run `docker`. 
    Then, whenever there is a `python runbenchmark.py ...` 
    command in the tutorial, add `-m docker` to it (`python runbenchmark.py ... -m docker`).

## Running the Benchmark

To run a benchmark call the `runbenchmark.py` script specifying the framework to evaluate.
See [integrated frameworks](#ADD) for a list of supported frameworks, or the [adding a frameworking](#ADD) page on how to add your own.

### Random Forest Test
Let's try evaluating the `RandomForest` baseline, which uses [scikit-learn](https://scikit-learn.org/stable/)'s random forest:

=== ":simple-linux: Linux", ":material-apple: MacOS"

    ```bash
    python runbenchmark.py randomforest 
    ```

=== ":simple-windows: Windows"
    As noted above, we need to install the AutoML frameworks (and baselines) in
    a container. Add `-m docker` to the command as shown:
    ```bash
    python runbenchmark.py randomforest -m docker
    ```
    Future example usages will only show the UNIX invocation, but will still require
    Windows users to add `-m docker`.

### Random Forest

`Benchmark`

: The benchmark suite is the dataset or set of datasets to evaluate the framework on.
  These can be defined as on [OpenML](https://www.openml.org) as a [study or task](#ADD-link-to-adding-openml-datasets) 
  (formatted as `openml/s/X` or `openml/t/Y` respectively) or in a [local file](#ADD-link-to-adding-local-benchmarks).


As you can see from the results above, the default behavior is to execute a short test benchmark.


`Constraints (optional, default='test')`

: The constraints applied to the benchmark as defined by default in [constraints.yaml](../resources/constraints.yaml). Default constraint is `test` (2 folds for 10 min each).

`Mode (optional, default='local')`

:  (Optional) If the benchmark should be run `local` (default, tested on Linux and macOS only), in a `docker` container or on `aws` using multiple ec2 instances.
