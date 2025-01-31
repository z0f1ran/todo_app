from datetime import datetime
from typing import Optional, List
from .base_item import BaseItem

class Task(BaseItem):
    priority_levels = {
        "low": 1,
        "normal": 2,
        "high": 3
    }
    
    def __init__(self, title: str, priority: str = "normal", description: str = ""):
        super().__init__(title)
        self.title = title
        self._priority = priority.lower()  # используем self
        self.description = description
        self.completed = False
        self.created_at = datetime.now()
        self.due_date: Optional[datetime] = None
        self.category = None
        self.subtasks: List['Task'] = []
        self.parent_task = None
        self.tags: set[str] = set()  # заменяем список на множество
    
    @property
    def priority(self) -> str:
        return self._priority
    
    @priority.setter
    def priority(self, value: str):
        if value.lower() not in self.priority_levels:
            raise ValueError("Недопустимый уровень приоритета")
        self._priority = value.lower()
    
    def display(self) -> str:
        status = "✓" if self.completed else " "
        category_name = self.category.name if self.category else "Без категории"
        tags = f" [{', '.join(self.tags)}]" if self.tags else ""
        return f"[{status}] {self.priority.upper()}: {self.title} ({category_name}){tags}"
    
    # Перегрузка операторов
    def __lt__(self, other: 'Task') -> bool:
        return self.priority_levels[self.priority] < self.priority_levels[other.priority]
    
    def __eq__(self, other: 'Task') -> bool:
        return self.title == other.title and self.priority == other.priority
    
    def __add__(self, other: str) -> 'Task':
        """Добавляет тег к задаче"""
        self.add_tag(other)
        return self
    
    def add_subtask(self, subtask: 'Task'):
        self.subtasks.append(subtask)
        subtask.parent_task = self
    
    def remove_subtask(self, subtask: 'Task'):
        if subtask in self.subtasks:
            self.subtasks.remove(subtask)
            subtask.parent_task = None
    
    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.add(tag)
    
    def remove_tag(self, tag: str):
        if tag in self.tags:
            self.tags.remove(tag)
    
    def complete(self):
        self.completed = True
        # Автоматически завершаем все подзадачи
        for subtask in self.subtasks:
            subtask.complete()
    
    def __str__(self):
        status = "✓" if self.completed else " "
        category_name = self.category.name if self.category else "Без категории"
        tags = f" [{', '.join(self.tags)}]" if self.tags else ""
        return f"[{status}] {self.priority.upper()}: {self.title} ({category_name}){tags}" 