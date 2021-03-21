# {{ cookiecutter.project_title }}

> {{ cookiecutter.project_description }}

[![Code style: black][black-img]][black-repo]
[![codecov][codecov-img]][codecov-project-link]
![Test][test-workflow-badge]

----

## Contents

:book:

> Note: Where ever you see the :book: icon you should be able to click on it and
> navigate back here to the table of contents.

- [Project Overview](#project-overview)
    - [Tech Stack](#tech-stack)
    - [Project Structure](#project-structure)
        - [Django & AWS Lambda](#django-aws-lambda)
- [Local Development](#local-development)
    - [Environment Setup](#environment-setup)
    - [How To Guides](#how-to-guides)
        - [Adding Apps](#adding-apps)
        - [Adding Commands](#adding-commands)

---

## Project Overview

### Tech Stack
[:book:](#contents)

#### API

* AWS CDK [:link:][aws-cdk-docs]
    * Lambda
    * RDS - Postgres
* Django [:link:][django-docs]
* Django REST Framework [:link:][drf-docs]

#### Documentation

* Sphinx [:link:][sphinx-docs] - Code
* DRF YASG [:link:][drf-yasg-docs] - API

#### CI/CD

* Github Actions [:link:][gh-actions-docs]
* CodeCov [:link:][codecov-docs]
* PyTest [:link:][pytest-docs]
* MyPy [:link:][mypy-docs]
* Flake8 [:link:][flake8-docs]
* Black [:link:][black-docs]

### Project Structure

[:book:](#contents)

_What's with the weird Django project structure?_

```
{{ cookiecutter.repo_name }}
|-- src
|   `-- {{ cookiecutter.src_package_name }}
|       |-- apps
|       |-- commands
|       |-- static
|       |-- templates
|       |-- utils
|       `-- manage.py, settings.py, etc...
|
|-- tests
|   |-- admin_tests
|   `-- unit_tests
|       |-- apps
|       |-- commands
|       `-- utils
|
|-- dev
|
|-- factories
|
|-- scripts
|
|-- documentation
|
|-- templates
|
|-- bin
|
|-- aws
|
`-- .github
```

**Short answer:** AWS Lambda.

**Long answer:**

By design Django does its best to tread the line between enabling the development
of reusable apps (i.e. models, views, admin) and providing a clear and flexible
framework for deploying production ready projects.

(point around the fact that this is a project implementation that leverages
Django and not a Django project that leverages a deployment architecture.)

* As flat and hopefully clear as possible using semantic naming structures.

Typically, Django projects are not deployed on top of the serverless AWS Lambda
infrastructure. This is normally true for a number of reasons, but the big
implementation questions are:

* How do you manage migrations without killing cold starts?
* How and when do you run Django commands?
* How is performance hurt by running Django in a Lambda function behind a VPC?

#### Django-AWS Lambda

> Lambda Layers, Custom Resources and CDK ftw!

Setting up the project code as a Lambda Layer

This allows the project as whole to be treated as a module and therefore can be
reused through AWS custom resources.

## Local Development

The following outlines brief details to help set up your local development
environment, as well as some guidelines around developer workflows.

### Environment Setup

[:book:](#contents)

> Note: This project assumes that you have both Docker and Docker Compose configured
> in your local environment. If you to install and configure them please follow the
> instructions listed [here][docker-compose-instructions].

#### Quick Start

`./bin/bootstrap`

#### Install Pyenv

It's recommended that you use `pyenv`, which you can read about more [here][pyenv-repo].

There is a [pyenv-installer][pyenv-installer] if you want to use that.
```bash
curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
```

#### Install Poetry

This project uses `poetry`, which you can read more about [here][poetry-home].
Install it using the following command.
```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```

If you would like to try different installation options there are more
instructions [here][poetry-installation-docs].

#### Install the dependencies

```shell
poetry install
```

#### Install pre-commit hooks

```shell
poetry run pre-commit install --hook-type commit-msg

poetry run pre-commit install
```

### How To Guides

[:book:](#contents)

Note that the following sections are just suggested guidelines that aim to help
elucidate common developer tasks and save time by offering utility scripts.

#### Adding Apps

```shell
poetry run startapp <app_name>
```

#### Running Tests

```shell
poetry run tests
```

#### Running a local server

```shell
poetry run server
```

#### Running Django Management Commands

```shell
poetry run manage makemigrations <app_name> <migration_name> ...
```

```shell
poetry run manage migrate
```

#### Adding Commands
TBD - coming soon

[black-img]: https://img.shields.io/badge/code%20style-black-000000.svg
[black-repo]: https://github.com/psf/black
[codecov-img]: https://codecov.io/gh/{{cookiecutter.github_username}}/{{cookiecutter.repo_name}}/branch/main/graph/badge.svg?token=JRCC98L3FG
[codecov-project-link]: https://codecov.io/gh/{{cookiecutter.github_username}}/{{cookiecutter.repo_name}}
[test-workflow-badge]: https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.repo_name}}/workflows/Test/badge.svg

[aws-cdk-docs]: https://docs.aws.amazon.com/cdk/api/latest/docs/aws-construct-library.html
[django-docs]: https://docs.djangoproject.com/en/3.1/
[drf-docs]: https://www.django-rest-framework.org/
[sphinx-docs]: https://www.sphinx-doc.org/en/master/
[drf-yasg-docs]: https://drf-yasg.readthedocs.io/en/stable/
[gh-actions-docs]: https://docs.github.com/en/actions
[codecov-docs]: https://docs.codecov.io/docs
[pytest-docs]: https://docs.pytest.org/en/stable/index.html
[mypy-docs]: http://mypy-lang.org/
[flake8-docs]: https://flake8.pycqa.org/en/latest/
[black-docs]: https://black.readthedocs.io/en/stable/

[docker-compose-instructions]: https://docs.docker.com/compose/install/

[pyenv-repo]: https://github.com/pyenv/pyenv
[pyenv-installer]: https://github.com/pyenv/pyenv-installer
[poetry-home]: https://python-poetry.org
[poetry-installation-docs]: https://python-poetry.org/docs/#installation

[lambda-layer-docs]: https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html
[lambda-layers-cdk-example]: https://docs.aws.amazon.com/cdk/api/latest/docs/aws-lambda-readme.html#layers

[python-lambda-function-cdk]: https://docs.aws.amazon.com/cdk/api/latest/docs/@aws-cdk_aws-lambda-python.PythonFunction.html
[python-lambda-layers-cdk]: https://docs.aws.amazon.com/cdk/api/latest/docs/@aws-cdk_aws-lambda-python.PythonLayerVersion.html

[custom-resources-docs]: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-custom-resources.html
[custom-resources-cdk]: https://docs.aws.amazon.com/cdk/api/latest/docs/custom-resources-readme.html

[aws-cdk-constructs]: https://docs.aws.amazon.com/cdk/api/latest/docs/@aws-cdk_core.ConstructNode.html
