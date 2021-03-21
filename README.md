# DRF AWS Lambda Project Template

Template for stand-alone Django REST Framework proof-of-concept projects
targeting a deployment to AWS Lambda + RDS Postgres.

## Getting Started

This is a `cookiecutter` template to read more about cookiecutter templates please refer
to the docs [here][cookiecutter-docs].

### CookieCutter Installation
It's recommended that you use `pyenv`, which you can read about more [here][pyenv-repo].

There is a [pyenv-installer][pyenv-installer] if you want to use that.
```bash
curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
```

Install a version of python, below is an example of how to do this.

```shell
pyenv install -s 3.8.6
```

Upgrade pip and install cookiecutter globally,

```shell
pip install --upgrade pip && pip install cookiecutter
```


## Usage

To use this template you can run the following command:

```shell
cookiecutter gh:anthonyalmarza/drf-lambda-project
```

### Template Options

- `repo_name` - The name of the base folder for the github repo. e.g. "my-drf-project"
- `project_title` - The display name for the project e.g. "My DRF Project"
- `project_description` - The short description for the project e.g. "A test drf project"
- `project_name` - The name used in the pyproject.toml file name key.
- `src_package_name` - The package name for the src folder.
- `project_domain` - The domain name to be used for the project.
- `author_name` - The author's name.
- `author_email` - The author's email address.
- `github_username` - The github username or organization where this project will live.


[cookiecutter-docs]: https://cookiecutter.readthedocs.io/en/1.7.2/
[pyenv-repo]: https://github.com/pyenv/pyenv
[pyenv-installer]: https://github.com/pyenv/pyenv-installer
