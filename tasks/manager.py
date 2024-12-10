from .storage import Storage
from rich.table import Table
from rich.console import Console


class TaskManager:
    def __init__(self, storage_file="tasks.json"):
        self.storage = Storage(storage_file)
        self.tasks = self.storage.load_tasks()

    def add_task(self, title, description, due_date):
        task_id = len(self.tasks) + 1
        task = {
            "id": task_id,
            "title": title,
            "description": description,
            "due_date": due_date,
            "completed": False,
        }
        self.tasks.append(task)
        self.storage.save_tasks(self.tasks)

    def list_tasks(self):
        table = Table(title="Task List")
        table.add_column("ID", justify="right")
        table.add_column("Title", style="bold")
        table.add_column("Description")
        table.add_column("Due Date")
        table.add_column("Completed", justify="center")
        for task in self.tasks:
            table.add_row(
                str(task["id"]),
                task["title"],
                task["description"],
                task["due_date"],
                "✔" if task["completed"] else "✘",
            )
        console = Console()
        console.print(table)

    def mark_complete(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                self.storage.save_tasks(self.tasks)
                return True
        return False

    def remove_task(self, task_id):
        self.tasks = [task for task in self.tasks if task["id"] != task_id]
        self.storage.save_tasks(self.tasks)
        return True
