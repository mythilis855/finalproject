import json
from pathlib import Path

def load_json_data(file_path):
    if not Path(file_path).exists():
        return []
    with open(file_path, "r") as f:
        return json.load(f)

def save_json_data(file_path, data):
    with open(file_path, "w") as f:
        json.dump(data, f)