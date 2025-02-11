from datetime import datetime
from .base_item import BaseItem

class Reminder(BaseItem):
    def __init__(self, title: str, due_date: datetime, description: str = ""):
        super().__init__(title)
        self.due_date = due_date
        self.description = description
        self.created_at = datetime.now()
        self.is_active = True
        self.is_triggered = False
        self.repeat_interval = None  # None, 'daily', 'weekly', 'monthly'
    
    def set_repeat(self, interval: str):
        valid_intervals = ['daily', 'weekly', 'monthly']
        if interval not in valid_intervals and interval is not None:
            raise ValueError("Недопустимый интервал повторения")
        self.repeat_interval = interval
    
    def deactivate(self):
        self.is_active = False
    
    def trigger(self):
        self.is_triggered = True
        if not self.repeat_interval:
            self.is_active = False
    
    def is_due(self) -> bool:
        return datetime.now() >= self.due_date and self.is_active and not self.is_triggered
    
    def __str__(self):
        status = "🔔" if self.is_active else "🔕"
        return f"{status} {self.title} (до {self.due_date.strftime('%d.%m.%Y %H:%M')})" 