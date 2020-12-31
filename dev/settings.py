# type: ignore
import socket
from CHANGE_ME.settings import *  # noqa

DEBUG = True

# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#email-host
EMAIL_HOST = env("EMAIL_HOST", default="mailhog")  # noqa: F405
# https://docs.djangoproject.com/en/dev/ref/settings/#email-port
EMAIL_PORT = env.int("EMAIL_PORT", default=1025)  # noqa: F405

ROOT_URLCONF = env("ROOT_URLCONF", default="dev.urls")  # noqa: F405

# django-debug-toolbar
# ------------------------------------------------------------------------------
hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS = [ip[:-1] + "1" for ip in ips]
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#prerequisites
INSTALLED_APPS += ["debug_toolbar"]  # noqa F405
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#middleware
MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware"
] + MIDDLEWARE  # noqa F405
# https://django-debug-toolbar.readthedocs.io/en/latest/configuration.html#debug-toolbar-config
DEBUG_TOOLBAR_CONFIG = {
    "DISABLE_PANELS": [
        "debug_toolbar.panels.redirects.RedirectsPanel",
    ],
    "SHOW_TEMPLATE_CONTEXT": True,
}

# django-extensions
# ------------------------------------------------------------------------------
# https://django-extensions.readthedocs.io/en/latest/installation_instructions.html#configuration
INSTALLED_APPS += ["django_extensions"]  # noqa F405


COMPRESS_OFFLINE = False
