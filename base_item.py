from abc import ABC, abstractmethod
from datetime import datetime

class BaseItem(ABC):
    _total_items = 0  # статическое поле для подсчета всех созданных элементов
    
    def __init__(self, name: str):
        self.name = name
        self.created_at = datetime.now()
        BaseItem._total_items += 1
    
    @abstractmethod
    def display(self) -> str:
        pass
    
    @staticmethod
    def get_total_items() -> int:
        return BaseItem._total_items
    
    def __str__(self) -> str:
        return self.display() 