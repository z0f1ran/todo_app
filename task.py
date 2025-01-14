from datetime import datetime

class Task:
    def __init__(self, title, priority="normal"):
        self.title = title
        self.priority = priority
        self.completed = False
        self.created_at = datetime.now()
    
    def complete(self):
        self.completed = True
    
    def __str__(self):
        status = "✓" if self.completed else " "
        return f"[{status}] {self.priority.upper()}: {self.title}" 