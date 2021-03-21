import sys

from drft.manage import manage_factory

from scripts.load_env import load_env

load_env()
manage = manage_factory()


def main():
    args = sys.argv[1:]
    return manage(*args)
