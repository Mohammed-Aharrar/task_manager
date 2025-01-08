"""
manager.py

Implements the TaskManager class to manage tasks with functionalities like add, list, complete, and remove.
"""

import logging  # Standard library import
from rich.table import Table  # Third-party imports
from rich.console import Console
from .storage import Storage  # Local imports

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="task_manager.log",
    filemode="a",
)
logger = logging.getLogger(__name__)


class TaskManager:
    """
    Manages tasks by providing functionalities to add, list, complete, and remove tasks.
    """

    def __init__(self, storage_file="tasks.json"):
        """
        Initializes the TaskManager with a storage file.

        Args:
            storage_file (str): The filename for storing tasks. Defaults to "tasks.json".
        """
        self.storage = Storage(storage_file)
        self.tasks = self.storage.load_tasks()
        logger.info("TaskManager initialized with storage file '%s'.", storage_file)

    def add_task(self, title, description, due_date):
        """
        Adds a new task to the task list.
        """
        logger.debug("Attempting to add task with title: '%s'.", title)
        if not title:
            logger.warning("Attempted to add a task without a title.")
            return
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
        logger.info("Task '%s' added successfully with ID %d.", title, task_id)

    def list_tasks(self):
        """
        Displays all tasks in a formatted table.
        """
        logger.debug("Listing all tasks.")
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
        logger.info("Displayed %d tasks.", len(self.tasks))

    def mark_complete(self, task_id):
        """
        Marks a task as complete based on its ID.
        """
        logger.debug("Marking task ID %d as complete.", task_id)
        for task in self.tasks:
            if task["id"] == task_id:
                if task["completed"]:
                    logger.warning("Task ID %d is already completed.", task_id)
                    return False
                task["completed"] = True
                self.storage.save_tasks(self.tasks)
                logger.info("Task ID %d marked as complete.", task_id)
                return True
        logger.error("Task ID %d not found.", task_id)
        return False

    def remove_task(self, task_id):
        """
        Removes a task from the task list based on its ID.
        """
        logger.debug("Attempting to remove task ID %d.", task_id)
        initial_count = len(self.tasks)
        self.tasks = [task for task in self.tasks if task["id"] != task_id]
        if len(self.tasks) < initial_count:
            self.storage.save_tasks(self.tasks)
            logger.info("Task ID %d removed successfully.", task_id)
            return True
        logger.error("Task ID %d not found. No task removed.", task_id)
        return False
