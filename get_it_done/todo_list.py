import sqlite3
from pathlib import Path
from task import Task

class Todo_List:
    def __init__(self):
        db = f"{Path(__file__).resolve().parent}/todolist.db"
        self.connect = sqlite3.connect(db)


    def new_list(self, name: str):
        pass

    
    def delete_list(self, name: str):
        pass


    def add_task(self, list: str, task: Task):
        pass
    

    def delete_task(self, list: str, task: Task):
        pass
