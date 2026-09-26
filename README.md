# Task Manager V2
V1.0.0

A simple CLI application for creating and managing tasks. Data is persisted in a JSON file.

---

## Structure

```text
app/
├── main.py
├── storage.py
├── exceptions.py
└── tasks.json

```

### `main.py`

Contains the core program logic:

* `Task` — The task class.
* `TaskStatus` — Task status enumeration.
* `TaskPriority` — Task priority enumeration.
* `create_task()` — Creates a new task.
* `list_tasks()` — Displays all tasks.
* `complete_task()` — Marks a task as completed.
* XP rewards depend on the task priority.

### `storage.py`

Handles data persistence with `tasks.json`.

Main functions:

```python
load_tasks()     # Loads tasks from the JSON file
save_tasks(tasks) # Saves tasks to the JSON file

```

### `exceptions.py`

Contains custom application exceptions.

Example:

```python
TaskNotFoundError  # Raised when attempting to find a non-existent task

```

### `tasks.json`

Stores saved tasks in JSON format.

Example:

```json
[
    {
        "id": 1,
        "title": "Learn Python",
        "description": "Study classes",
        "priority": "high",
        "status": "pending",
        "xp": 30
    }
]

```

---

## Features

1. **Create task** — Add a new task to your list.
2. **List tasks** — View all existing tasks.
3. **Complete task** — Mark a task as finished and earn XP.
4. **Exit** — Quit the application.

---

## XP System

Each priority level awards a specific amount of XP upon completion:

| Priority | XP |
| --- | --- |
| Low | 10 |
| Medium | 20 |
| High | 30 |
| Urgent | 50 |
