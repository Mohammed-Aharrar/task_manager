"""
cli.py

Provides a Command Line Interface (CLI) for managing tasks.
"""

import click  # Third-party import
import logging  # Standard library import
from tasks.manager import TaskManager  # Local import

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="cli.log",
    filemode="a",
)
logger = logging.getLogger(__name__)

manager = TaskManager()


@click.group()
def cli():
    """
    Task Management System CLI.

    Provides commands to add, list, complete, and remove tasks.
    """
    logger.info("CLI invoked.")


@cli.command()
@click.option("--title", prompt="Title", help="Title of the task")
@click.option("--description", prompt="Description", help="Description of the task")
@click.option(
    "--due_date", prompt="Due Date", help="Due date of the task in 'YYYY-MM-DD' format"
)
def add(title, description, due_date):
    """
    Add a new task to the Task Manager.

    Args:
        title (str): The title of the task.
        description (str): A brief description of the task.
        due_date (str): The due date for the task.
    """
    logger.debug(
        "Add command called with title: '%s', description: '%s', due_date: '%s'.",
        title,
        description,
        due_date,
    )
    try:
        manager.add_task(title, description, due_date)
        click.echo(f"Task '{title}' added!")
        logger.info("Task '%s' added via CLI.", title)
    except ValueError as e:
        logger.error("Invalid input: %s", e)
        click.echo("Invalid input. Please try again.")
    except Exception as e:
        logger.critical("Failed to add task: %s", e)
        click.echo("An error occurred while adding the task.")


@cli.command()
def list_tasks():
    """
    List all tasks in the Task Manager.
    """
    logger.debug("List command called.")
    try:
        manager.list_tasks()
        logger.info("Tasks listed via CLI.")
    except FileNotFoundError as e:
        logger.error("File not found: %s", e)
        click.echo("Storage file not found.")
    except Exception as e:
        logger.critical("Failed to list tasks: %s", e)
        click.echo("An error occurred while listing tasks.")


@cli.command()
@click.argument("task_id", type=int)
def complete(task_id):
    """
    Mark a specific task as complete.

    Args:
        task_id (int): The ID of the task to mark as complete.
    """
    logger.debug("Complete command called for task ID: %d.", task_id)
    try:
        if manager.mark_complete(task_id):
            click.echo(f"Task {task_id} marked as complete.")
            logger.info("Task ID %d marked as complete via CLI.", task_id)
        else:
            click.echo("Task not found or already completed.")
            logger.warning("Failed to mark Task ID %d as complete.", task_id)
    except Exception as e:
        logger.critical("Failed to complete task ID %d: %s", task_id, e)
        click.echo("An error occurred while completing the task.")


@cli.command()
@click.argument("task_id", type=int)
def remove(task_id):
    """
    Remove a specific task from the Task Manager.

    Args:
        task_id (int): The ID of the task to remove.
    """
    logger.debug("Remove command called for task ID: %d.", task_id)
    try:
        if manager.remove_task(task_id):
            click.echo(f"Task {task_id} removed.")
            logger.info("Task ID %d removed via CLI.", task_id)
        else:
            click.echo("Task not found.")
            logger.warning("Failed to remove Task ID %d.", task_id)
    except Exception as e:
        logger.critical("Failed to remove task ID %d: %s", task_id, e)
        click.echo("An error occurred while removing the task.")


if __name__ == "__main__":
    try:
        cli()
    except Exception as e:
        logger.critical("CLI terminated unexpectedly: %s", e)
