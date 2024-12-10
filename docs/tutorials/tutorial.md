# Task Manager Tutorial: Organizing Your Day

In this tutorial, we will learn to manage tasks using the Task Manager application. By the end, you will know how to create tasks, list them, mark them as complete, and remove unnecessary tasks. 

## Step 1: Set Up the Task Manager

Before we start managing tasks, we need to set up the Task Manager. Open your terminal and follow these steps:

1. Clone the repository and navigate to it:
   ```bash
   git clone https://github.com/Mohammed-Aharrar/task_manager.git
   cd task_manager
   ```

2. Install all necessary dependencies:
   ```bash
   poetry install
   ```

> **Expected Result:** After running the commands, your environment is ready to use the Task Manager.

## Step 2: Add and List Tasks

Now, let’s create a new task to remember an important activity:

1. Add a new task:
   ```bash
   poetry run python cli.py add --title "Plan Meeting" --description "Discuss project updates" --due_date "2024-12-15"
   ```

2. List all tasks to confirm it was added:
   ```bash
   poetry run python cli.py list
   ```

> **Expected Result:** The task "Plan Meeting" should appear in the task list. Notice the details like title, description, due date, and the incomplete status (✘).

## Step 3: Mark a Task as Complete

Once you’ve finished a task, you can mark it as complete:

1. Use the task ID from the list to mark it as done:
   ```bash
   poetry run python cli.py complete <task_id>
   ```

2. Check the task list again:
   ```bash
   poetry run python cli.py list
   ```

> **Expected Result:** The task you marked as complete will show a ✔ in the "Completed" column.


## Step 4: Remove a Task

If a task is no longer needed, you can easily remove it from the list:

1. Use the task ID from the list to delete the task:
   ```bash
   poetry run python cli.py remove <task_id>
   ```

2. Verify that the task has been removed by listing all tasks again:
   ```bash
   poetry run python cli.py list
   ```

> **Expected Result:** The task with the specified ID will no longer appear in the task list.
