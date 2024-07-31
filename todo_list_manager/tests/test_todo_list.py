import pytest
from todo_list import ToDoListManager

def test_add_task():
    manager = ToDoListManager()
    manager.add_task("Buy groceries")
    tasks = manager.list_tasks()
    assert len(tasks) == 1
    assert tasks[0].name == "Buy groceries"

def test_list_tasks():
    manager = ToDoListManager()
    manager.add_task("Buy groceries")
    manager.add_task("Pay bills")
    tasks = manager.list_tasks()
    assert len(tasks) == 2

def test_mark_task_as_completed():
    manager = ToDoListManager()
    manager.add_task("Buy groceries")
    manager.mark_task_as_completed("Buy groceries")
    tasks = manager.list_tasks()
    assert tasks[0].status == "Completed"

def test_edit_task():
    manager = ToDoListManager()
    manager.add_task("Buy groceries", "2024-08-01", "High")
    manager.edit_task("Buy groceries", new_name="Buy food", new_due_date="2024-08-02")
    tasks = manager.list_tasks()
    task = next(task for task in tasks if task.name == "Buy food")
    assert task.due_date == "2024-08-02"

def test_clear_tasks():
    manager = ToDoListManager()
    manager.add_task("Buy groceries")
    manager.clear_tasks()
    tasks = manager.list_tasks()
    assert len(tasks) == 0
