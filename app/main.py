import storage as data
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

tasks = data.load_tasks()
print(tasks)

    

    
    
    