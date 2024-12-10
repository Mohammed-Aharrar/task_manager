import json
import os


class Storage:
    def __init__(self, filename):
        self.filename = filename

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                return json.load(f)
        return []

    def save_tasks(self, tasks):
        with open(self.filename, "w") as f:
            json.dump(tasks, f, indent=4)
