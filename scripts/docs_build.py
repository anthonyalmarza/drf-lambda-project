import subprocess
import sys


def main():
    subprocess.run(
        ["sphinx-build", "documentation/", "docs/"] + sys.argv[1:], check=True
    )
