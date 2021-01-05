import os
import subprocess
import sys

from drft.manage import manage_factory

from scripts.load_env import load_env

load_env()
manage = manage_factory()


DJANGO_AUTORELOAD_ENV = "RUN_MAIN"


def restart_with_reloader():
    new_environ = {**os.environ, DJANGO_AUTORELOAD_ENV: "true"}
    args = ["poetry", "run", "manage", "runserver"] + sys.argv[1:]
    while True:
        p = subprocess.run(args, env=new_environ, close_fds=False)
        if p.returncode != 3:
            return p.returncode


def main():
    manage("collectstatic", "--noinput")
    manage("compress", "--force")
    if "--noreload" in sys.argv[1:]:
        return manage("runserver", sys.argv[1:])
    return restart_with_reloader()
