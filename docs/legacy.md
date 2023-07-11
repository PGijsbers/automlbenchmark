Installation:

or using pyenv:
```bash
pyenv install {python_version: 3.9.16}
pyenv virtualenv ve-automl
pyenv local ve-automl
```

- _**NOTE**: in case of issues when installing Python requirements, you may want to try the following:_
    - _on some platforms, we need to ensure that requirements are installed sequentially:_ `xargs -L 1 python -m pip install < requirements.txt`.
    - _enforce the `python -m pip` version above in your virtualenv:_ `python -m pip install --upgrade pip==19.3.1`.


