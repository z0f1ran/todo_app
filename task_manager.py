from datetime import datetime
from typing import List, Dict, Optional
from .task import Task
from .task_category import TaskCategory

class TaskManager:
    def __init__(self):
        self.tasks: List[Task] = []
        self.categories: List[TaskCategory] = []
        self.tags: List[str] = []
    
    def add_category(self, name: str, description: str = "") -> TaskCategory:
        category = TaskCategory(name, description)
        self.categories.append(category)
        return category
    
    def remove_category(self, category: TaskCategory):
        if category in self.categories:
            # Перемещаем задачи в категорию "Без категории"
            for task in category.tasks:
                task.category = None
            self.categories.remove(category)
    
    def add_task(self, title: str, priority: str = "normal", category: Optional[TaskCategory] = None) -> Task:
        task = Task(title, priority)
        if category:
            category.add_task(task)
        self.tasks.append(task)
        return task
    
    def add_subtask(self, parent_task: Task, title: str, priority: str = "normal") -> Task:
        subtask = Task(title, priority)
        parent_task.add_subtask(subtask)
        self.tasks.append(subtask)
        return subtask
    
    def list_tasks(self, category: Optional[TaskCategory] = None) -> str:
        if not self.tasks:
            return "Нет задач"
        
        tasks_to_show = self.tasks
        if category:
            tasks_to_show = category.tasks
            
        return "\n".join(str(task) for task in tasks_to_show)
    
    def list_categories(self) -> str:
        if not self.categories:
            return "Нет категорий"
        return "\n".join(str(category) for category in self.categories)
    
    def find_tasks_by_tag(self, tag: str) -> List[Task]:
        return [task for task in self.tasks if tag in task.tags]
    
    def complete_task(self, index: int) -> bool:
        if 0 <= index < len(self.tasks):
            self.tasks[index].complete()
            return True
        return False
    
    def remove_task(self, index: int) -> bool:
        if 0 <= index < len(self.tasks):
            task = self.tasks[index]
            if task.category:
                task.category.remove_task(task)
            if task.parent_task:
                task.parent_task.remove_subtask(task)
            self.tasks.pop(index)
            return True
        return False 