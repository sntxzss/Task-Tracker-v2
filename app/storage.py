import json
from pathlib import Path

FILE_PATH = Path("tasks.json")


def load_tasks():
    if not FILE_PATH.exists():
        return []

    with open(FILE_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


def save_tasks(tasks):
    with open(FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4, ensure_ascii=False)

tasks = []
