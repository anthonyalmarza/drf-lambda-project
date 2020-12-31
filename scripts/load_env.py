import os
from dotenv import load_dotenv


def load_env():
    dotenv_path = os.environ.get("DOTENV_PATH", "dev/dev.env")
    load_dotenv(dotenv_path=dotenv_path)
