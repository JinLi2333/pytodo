from datetime import datetime
from models.todo_step import TodoStep

from enum import Enum, auto

class RepeatMode(Enum):
    day = auto()
    weekday = auto
    week = auto()
    month = auto()
    year = auto()
    custom = auto()


class Todo:
    def __init__(self,
                 title: str,
                 is_completed: bool,
                 is_favorite: bool,
                 steps: list[TodoStep] | None = None,
                 deadline: datetime | None = None,
                 repeat_mode: str | None = None,
                 assign_to: str | None = None) -> None:
        self.title: str = title
        self.is_completed: bool = is_completed
        self.is_favorite: bool = is_favorite
        self.steps: list[TodoStep] | None = steps
        self.deadline: datetime | None = deadline
        self.repeat_mode: str | None = repeat_mode
        self.assign_to: str | None = assign_to

    def display(self) -> None:
        print(f"{self.title}")