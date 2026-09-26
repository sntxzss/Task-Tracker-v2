import storage

from enum import Enum

from exceptions import TaskNotFoundError


class TaskStatus(Enum):
    PENDING = "pending"
    COMPLETED = "completed"


class TaskPriority(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    URGENT = "urgent"


XP_BY_PRIORITY = {
    TaskPriority.LOW: 10,
    TaskPriority.MEDIUM: 20,
    TaskPriority.HIGH: 30,
    TaskPriority.URGENT: 50
}


class Task:
 def __init__(self, id, title, description, priority):
    self.id = id
    self.title = title
    self.description = description
    self.priority = priority
    self.status = TaskStatus.PENDING
    self.xp = XP_BY_PRIORITY[priority]

 def complete(self):
    self.status = TaskStatus.COMPLETED

 def uncomplete(self):
    self.status = TaskStatus.PENDING

 def to_storage(self):
    return {
        "id": self.id,
        "title": self.title,
        "description": self.description,
        "priority": self.priority.value,
        "status": self.status.value,
        "xp": self.xp
    }
 def create_task():
    tasks = storage.load_tasks()
    title = input("Title: ")
    description = input("Description: ")
    priority_input = input("Priority (low/medium/high/urgent): ").lower()
    priority = TaskPriority(priority_input)
    new_id = len(tasks) + 1
    task = Task(
        new_id,
        title,
        description,
        priority
    )
    tasks.append(task.to_storage())
    storage.save_tasks(tasks)
    print("Task created")

    def load_tasks():
       tasks = storage.load_tasks()

       if not tasks:
          print("No tasks")
          return

    for tasks in tasks:
       print(
            f"{task['id']}. "
            f"{task['title']} | "
            f"{task['priority']} | "
            f"{task['status']} | "
            f"{task['xp']} XP"
        )

    def complete_task():
     tasks = storage.load_tasks()
     task_id = int(input("Task ID: "))
     for task in tasks:
        if task["id"] == task_id:
            task["status"] = TaskStatus.COMPLETED.value
            storage.save_tasks(tasks)
            print("Task completed!")
            return
     raise TaskNotFoundError("Task not found.")

while True:
    print()
    print("1. Create task")
    print("2. List tasks")
    print("3. Complete task")
    print("4. Exit")
    choice = input("Choose: ")
    if choice == "1":
        create_task()
    elif choice == "2":
        list_tasks()
    elif choice == "3":
        try:
            complete_task()
        except TaskNotFoundError as error:
            print(error)
    elif choice == "4":
        break
    else:
        print("Invalid choice.")