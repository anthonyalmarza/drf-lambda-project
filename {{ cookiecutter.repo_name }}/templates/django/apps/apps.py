{% raw %}from django.apps import AppConfig


class {{ camel_case_app_name|title }}Config(AppConfig):
    name = {% endraw %}"{{ cookiecutter.src_package_name }}{% raw %}.apps.{{ app_name }}"{% endraw %}
