from dataclasses import dataclass

@dataclass
class Task:
    task: str
    description: str = None
    due: str = None
    complete: bool = False