from datetime import datetime
from typing import Set, Dict, Optional, List
from .task import Task
from .task_category import TaskCategory
from .note import Note
from .reminder import Reminder

class TaskManagerException(Exception):
    pass

class TaskManager:
    def __init__(self):
        self.tasks: Set[Task] = set()  # используем множество
        self.categories: Set[TaskCategory] = set()
        self.tags: Set[str] = set()
        self.notes: Set[Note] = set()
        self.reminders: Set[Reminder] = set()
    
    def add_category(self, name: str, description: str = "") -> TaskCategory:
        try:
            if any(c.name == name for c in self.categories):
                raise TaskManagerException(f"Категория '{name}' уже существует")
            category = TaskCategory(name, description)
            self.categories.add(category)
            return category
        except Exception as e:
            raise TaskManagerException(f"Ошибка при создании категории: {str(e)}")
    
    def remove_category(self, category: TaskCategory):
        if category in self.categories:
            # Перемещаем задачи в категорию "Без категории"
            for task in category.tasks:
                task.category = None
            self.categories.remove(category)
    
    def add_task(self, title: str, priority: str = "normal", category: Optional[TaskCategory] = None) -> Task:
        try:
            task = Task(title, priority)
            if category:
                if category not in self.categories:
                    raise TaskManagerException("Указанная категория не существует")
                category.add_task(task)
            self.tasks.add(task)
            return task
        except ValueError as e:
            raise TaskManagerException(f"Ошибка при создании задачи: {str(e)}")
    
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
    
    def add_note(self, title: str, content: str = "") -> Note:
        try:
            note = Note(title, content)
            self.notes.add(note)
            return note
        except Exception as e:
            raise TaskManagerException(f"Ошибка при создании заметки: {str(e)}")
    
    def add_reminder(self, title: str, due_date: datetime, description: str = "") -> Reminder:
        try:
            reminder = Reminder(title, due_date, description)
            self.reminders.add(reminder)
            return reminder
        except Exception as e:
            raise TaskManagerException(f"Ошибка при создании напоминания: {str(e)}")
    
    def list_notes(self) -> str:
        if not self.notes:
            return "Нет заметок"
        return "\n".join(str(note) for note in self.notes)
    
    def list_reminders(self) -> str:
        if not self.reminders:
            return "Нет напоминаний"
        return "\n".join(str(reminder) for reminder in self.reminders)
    
    def check_due_reminders(self) -> List[Reminder]:
        """Возвращает список просроченных активных напоминаний"""
        return [r for r in self.reminders if r.is_due()]