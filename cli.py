import click
from tasks.manager import TaskManager

manager = TaskManager()


@click.group()
def cli():
    """Task Management System"""
    pass


@cli.command()
@click.option("--title", prompt="Title", help="Title of the task")
@click.option("--description", prompt="Description", help="Description of the task")
@click.option("--due_date", prompt="Due Date", help="Due date of the task")
def add(title, description, due_date):
    """Add a new task"""
    manager.add_task(title, description, due_date)
    click.echo(f"Task '{title}' added!")


@cli.command()
def list():
    """List all tasks"""
    manager.list_tasks()


@cli.command()
@click.argument("task_id", type=int)
def complete(task_id):
    """Mark a task as complete"""
    if manager.mark_complete(task_id):
        click.echo(f"Task {task_id} marked as complete.")
    else:
        click.echo("Task not found.")


@cli.command()
@click.argument("task_id", type=int)
def remove(task_id):
    """Remove a task"""
    if manager.remove_task(task_id):
        click.echo(f"Task {task_id} removed.")
    else:
        click.echo("Task not found.")


if __name__ == "__main__":
    cli()
