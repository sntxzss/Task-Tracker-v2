from pathlib import Path
import json

FILE_NAME = Path(__file__).parent / "tasks.json"


def load_tasks():
    if not FILE_NAME.exists():
        return []

    with open(FILE_NAME, "r", encoding="utf-8") as file:
        return json.load(file)


def save_tasks(tasks):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)