# drf-lambda-project

Template for Django REST Framework projects built on top of AWS Lambda


[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![codecov](https://codecov.io/gh/anthonyalmarza/CHANGE_ME/branch/main/graph/badge.svg?token=JRCC98L3FG)](https://codecov.io/gh/anthonyalmarza/CHANGE_ME)

![Test](https://github.com/anthonyalmarza/CHANGE_ME/workflows/Test/badge.svg)

## Local Development

### Pyenv
It's recommended that you use [`pyenv`](https://github.com/pyenv/pyenv)

[pyenv-installer](https://github.com/pyenv/pyenv-installer)
```bash
curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
```

### Install `poetry`

This project uses [`poetry`](https://python-poetry.org). Install it using the following command.
```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```
More instructions [here](https://python-poetry.org/docs/#installation)

### Install the dependencies:

`poetry install`

Install pre-commit hooks:

`poetry run pre-commit install`

### Running Tests:

`poetry run tests`
