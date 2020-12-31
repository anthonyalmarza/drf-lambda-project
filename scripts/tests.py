import subprocess
import sys

import coverage
import pytest

from scripts.load_env import load_env

load_env()

subprocess.run(["docker-compose", "up", "-d"], check=True)


def main():
    cov = coverage.Coverage()
    cov.start()
    pytest.main(sys.argv[1:])
    cov.stop()
    cov.save()
    cov.report()
