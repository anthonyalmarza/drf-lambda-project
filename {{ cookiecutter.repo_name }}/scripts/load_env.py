import os
import subprocess

from dotenv import load_dotenv


def load_env():
    if os.environ.get("CI") != "true":
        subprocess.run(["docker-compose", "up", "-d"], check=True)

    dotenv_path = os.environ.get("DOTENV_PATH", "dev/dev.env")
    load_dotenv(dotenv_path=dotenv_path)
