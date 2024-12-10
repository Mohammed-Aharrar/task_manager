# Task Manager

This CLI-based Task Manager is built using Python and managed with Poetry. It allows users to add, view, complete, and remove tasks, storing all task information persistently.

## Features

- **Add Tasks**: Users can create tasks with titles, descriptions, and due dates.
- **List Tasks**: Displays all tasks in a table format.
- **Complete Tasks**: Allows marking tasks as done.
- **Remove Tasks**: Enables deleting tasks from the list.

## Prerequisites

Make sure you have installed:
- Python 3.9 or higher
- Poetry for handling the project and dependencies

## Installation

Follow these steps to set up the Task Manager on your computer:

1. **Clone the Repository**:
git clone https://github.com/Mohammed-Aharrar/task_manager.git
cd task_manager




2. **Install Dependencies**:
Install all necessary libraries using Poetry.
poetry install



## Static Code Analysis

To ensure code quality and maintain consistent formatting, this project utilizes **Flake8** and **Black** for static code analysis. After installing the dependencies, you can perform linting with Flake8 and check or format your code with Black.

- **Run Static Analysis**:
  - **Flake8** (Linting):
    ```bash
    poetry run flake8 .
    ```

  - **Black** (Formatting Check):
    ```bash
    poetry run black --check .
    ```

  - **Black** (Auto-formatting):
    ```bash
    poetry run black .
    ```
- **Automatic Execution**

    Black and Flake8 will automatically run on staged files every time you execute git commit. If any issues are detected, the commit will be blocked until they are resolved.

## Unit Testing

We use `pytest` for unit testing to ensure the reliability of the Task Manager's functionalities. To run the tests located in `tests/test_manager.py`, use the following command:

```bash
poetry run pytest tests/test_manager.py
```

## Building the Project

Build the project to make a package:
poetry build



This command makes a `.whl` file and a source archive in the `dist` directory.

## Documentation

We use `pdoc` to generate reference documentation from the Python docstrings. To generate the documentation in docs folder we use the following command:
```bash
poetry run pdoc tasks cli --output-dir docs
```


## License

This project is under the MIT License. See the [LICENSE](LICENSE) file for details.
