from datetime import datetime
from typing import List

class TaskCategory:
    def __init__(self, name: str, description: str = ""):
        self.name = name
        self.description = description
        self.created_at = datetime.now()
        self.tasks: List['Task'] = []

    def add_task(self, task: 'Task'):
        self.tasks.append(task)
        task.category = self

    def remove_task(self, task: 'Task'):
        if task in self.tasks:
            self.tasks.remove(task)
            task.category = None

    def __str__(self):
        return f"Категория: {self.name} ({len(self.tasks)} задач)" 