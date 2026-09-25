import storage as data
from enum import Enum
from exceptions import TaskNotFoundError

class Task:
    def __init__(self, id, title, description, status, priority, xp):
        self.id = id
        self.title = title
        self.description = description
        self.status = status
        self.priority = priority
        self.xp = xp
        self.completed = False

    class task_status(Enum):
      PENDING = "pending"
      COMPLETED = "completed"

    class task_priority(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    URGENT = "urgent"
    
    def to_storage(self):
       return {
           "ID": self.id,
           "title": self.title,
           "description": self.description,
           "status": self.status,
           "priority": self.priority,
           "completed": self.completed,
           "xp": self.xp
       }
    
    def complete(self):
        self.completed = True

    def uncomplete(self):
        self.completed = False

    def load_tasks(self):
        for task_list in data.tasks:
            print(task_list)

    def create_task(self):
        self.to_storage["ID"] = len(data.tasks) + 1
        self.to_storage["title"] = str(input("Enter title:"))
        self.to_storage["description"] = str(input("Enter description:"))
        self.to_storage["status"] = self.task_status.PENDING
        self.to_storage["priority"] = input(("Enter your priority (LOW/MEDIUM/HIGH/URGENT): "))
    

    
    
    