from datetime import datetime
from typing import Optional, List

class Task:
    def __init__(self, title: str, priority: str = "normal", description: str = ""):
        self.title = title
        self.priority = priority
        self.description = description
        self.completed = False
        self.created_at = datetime.now()
        self.due_date: Optional[datetime] = None
        self.category = None
        self.subtasks: List['Task'] = []
        self.parent_task = None
        self.tags: List[str] = []
    
    def add_subtask(self, subtask: 'Task'):
        self.subtasks.append(subtask)
        subtask.parent_task = self
    
    def remove_subtask(self, subtask: 'Task'):
        if subtask in self.subtasks:
            self.subtasks.remove(subtask)
            subtask.parent_task = None
    
    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)
    
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