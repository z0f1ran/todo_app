from datetime import datetime
from task import Task

class TaskManager:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, title, priority="normal"):
        task = Task(title, priority)
        self.tasks.append(task)
        return task
    
    def list_tasks(self):
        if not self.tasks:
            return "Нет задач"
        return "\n".join(str(task) for task in self.tasks)
    
    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].complete()
            return True
        return False
    
    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            return True
        return False 