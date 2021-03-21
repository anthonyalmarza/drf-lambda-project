import os
import sys

from drft.manage import manage_factory
from scripts.load_env import load_env

load_env()
manage = manage_factory()


def start_app(app_name: str):
    app_path = 'src/{{cookiecutter.src_package_name}}/apps/' + app_name
    tests_path = 'tests/unit_tests/apps/' + app_name
    os.makedirs(app_path, exist_ok=True)
    manage(
        'startapp',
        '--template=templates/django/apps',
        app_name,
        app_path
    )
    os.makedirs(tests_path, exist_ok=True)
    manage(
        'startapp',
        '--template=templates/django/tests/unit_tests',
        app_name,
        tests_path
    )


def main():
    app_name = sys.argv[1]
    return start_app(app_name)
