import sys

import coverage
import pytest

from scripts.load_env import load_env

load_env()


def main():
    cov = coverage.Coverage()
    cov.start()
    status = pytest.main(sys.argv[1:])
    if status != pytest.ExitCode.OK:
        sys.exit(status)
    cov.stop()
    cov.save()
    total_coverage = cov.report()
    if total_coverage < cov.config.fail_under:
        print(
            f"Coverage failure: {int(total_coverage)} is less than "
            f"fail-under={cov.config.fail_under}"
        )
        sys.exit(1)
