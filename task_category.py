from datetime import datetime
from typing import List, Set
from .base_item import BaseItem

class TaskCategory(BaseItem):
    categories_count = 0  # статическое поле
    
    def __init__(self, name: str, description: str = ""):
        super().__init__(name)
        self.description = description
        self.tasks: Set['Task'] = set()  # используем множество вместо списка
        TaskCategory.categories_count += 1
    
    @staticmethod
    def get_categories_count() -> int:
        return TaskCategory.categories_count
    
    def display(self) -> str:
        return f"Категория: {self.name} ({len(self.tasks)} задач)"

    def add_task(self, task: 'Task'):
        self.tasks.append(task)
        task.category = self

    def remove_task(self, task: 'Task'):
        if task in self.tasks:
            self.tasks.remove(task)
            task.category = None

    def __str__(self):
        return f"Категория: {self.name} ({len(self.tasks)} задач)" 