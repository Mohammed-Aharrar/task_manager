import pytest
from tasks.manager import TaskManager


@pytest.fixture
def task_manager(tmp_path):
    # Setup: Create a temporary storage file
    storage_file = tmp_path / "test_tasks.json"
    manager = TaskManager(storage_file=str(storage_file))
    return manager


def test_add_task(task_manager):
    initial_count = len(task_manager.tasks)
    task_manager.add_task("Test Task", "Test Description", "2024-12-31")
    assert len(task_manager.tasks) == initial_count + 1
    assert task_manager.tasks[-1]["title"] == "Test Task"


def test_mark_complete(task_manager):
    task_manager.add_task("Complete Task", "To be completed", "2024-12-31")
    task_id = task_manager.tasks[-1]["id"]
    result = task_manager.mark_complete(task_id)
    assert result is True
    assert task_manager.tasks[-1]["completed"] is True


def test_remove_task(task_manager):
    task_manager.add_task("Remove Task", "To be removed", "2024-12-31")
    task_id = task_manager.tasks[-1]["id"]
    initial_count = len(task_manager.tasks)
    result = task_manager.remove_task(task_id)
    assert result is True
    assert len(task_manager.tasks) == initial_count - 1
    assert not any(task["id"] == task_id for task in task_manager.tasks)


def test_mark_nonexistent_task_complete(task_manager):
    result = task_manager.mark_complete(999)
    assert result is False


def test_remove_nonexistent_task(task_manager):
    result = task_manager.remove_task(999)
    assert result is False
