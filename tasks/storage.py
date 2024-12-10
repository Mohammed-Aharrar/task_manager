import json
import os


class Storage:
    """
    Handles loading and saving tasks to a JSON file.

    Attributes:
        filename (str): The name of the JSON file used for storage.
    """

    def __init__(self, filename):
        """
        Initializes the Storage with a specified filename.

        Args:
            filename (str): The name of the JSON file.
        """
        self.filename = filename

    def load_tasks(self):
        """
        Loads tasks from the JSON storage file.

        Returns:
            list: A list of task dictionaries.
        """
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                return json.load(f)
        return []

    def save_tasks(self, tasks):
        """
        Saves the current list of tasks to the JSON storage file.

        Args:
            tasks (list): A list of task dictionaries to save.
        """
        with open(self.filename, "w") as f:
            json.dump(tasks, f, indent=4)
