import json
from pathlib import Path

CONFIG_FILE = Path(__file__).parent / "config.json"

with open(CONFIG_FILE, "r") as f:
    CONFIG = json.load(f)