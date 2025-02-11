from datetime import datetime
from .base_item import BaseItem

class Note(BaseItem):
    def __init__(self, title: str, content: str = ""):
        super().__init__(title)
        self.content = content
        self.created_at = datetime.now()
        self.last_modified = self.created_at
        self.tags: set[str] = set()
    
    def edit_content(self, new_content: str):
        self.content = new_content
        self.last_modified = datetime.now()
    
    def add_tag(self, tag: str):
        self.tags.add(tag)
    
    def remove_tag(self, tag: str):
        if tag in self.tags:
            self.tags.remove(tag)
    
    def __str__(self):
        tags = f" [{', '.join(self.tags)}]" if self.tags else ""
        preview = (self.content[:50] + '...') if len(self.content) > 50 else self.content
        return f"📝 {self.title}{tags}\n   {preview}" 