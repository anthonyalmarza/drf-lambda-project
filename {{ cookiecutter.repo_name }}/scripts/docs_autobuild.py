import subprocess
import sys


def main():
    subprocess.run(
        ["sphinx-autobuild", "documentation/", "docs/"] + sys.argv[1:],
        check=True,
    )
