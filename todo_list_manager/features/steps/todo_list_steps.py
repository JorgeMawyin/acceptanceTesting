from behave import given, when, then
from todo_list import ToDoListManager

@given('the to-do list is empty')
def step_given_todo_list_is_empty(context):
    context.manager = ToDoListManager()

@when('the user adds a task "{task_name}"')
def step_when_user_adds_task(context, task_name):
    context.manager.add_task(task_name)

@then('the to-do list should contain "{task_name}"')
def step_then_todo_list_should_contain(context, task_name):
    tasks = context.manager.list_tasks()
    assert any(task.name == task_name for task in tasks), f'Task "{task_name}" not found in the to-do list'

@given('the to-do list contains tasks')
def step_given_todo_list_contains_tasks(context):
    context.manager = ToDoListManager()
    for row in context.table:
        # Parse the task attributes from the table
        name = row['Task']
        due_date = row.get('Due Date')
        priority = row.get('Priority')
        context.manager.add_task(name, due_date, priority)

@when('the user lists all tasks')
def step_when_user_lists_all_tasks(context):
    context.tasks = context.manager.list_tasks()

@then('the output should contain')
def step_then_output_should_contain(context):
    expected_output = context.text.strip().split('\n')[1:]
    actual_output = [f"- {task.name}" for task in context.tasks]
    assert expected_output == actual_output, f"Expected: {expected_output}, but got: {actual_output}"

@when('the user marks task "{task_name}" as completed')
def step_when_user_marks_task_as_completed(context, task_name):
    context.manager.mark_task_as_completed(task_name)

@then('the to-do list should show task "{task_name}" as completed')
def step_then_todo_list_should_show_task_as_completed(context, task_name):
    task = next(task for task in context.manager.list_tasks() if task.name == task_name)
    assert task.status == "Completed", f'Task "{task_name}" is not marked as completed'

@when('the user edits the task "{old_name}" to have new name "{new_name}" and new due date "{new_due_date}"')
def step_when_user_edits_task(context, old_name, new_name, new_due_date):
    context.manager.edit_task(old_name, new_name=new_name, new_due_date=new_due_date)

@then('the to-do list should contain a task with name "{new_name}" and due date "{new_due_date}"')
def step_then_todo_list_should_contain_edited_task(context, new_name, new_due_date):
    task = next(task for task in context.manager.list_tasks() if task.name == new_name)
    assert task.due_date == new_due_date, f'Task "{new_name}" does not have the due date "{new_due_date}"'

@when('the user clears the to-do list')
def step_when_user_clears_todo_list(context):
    context.manager.clear_tasks()

@then('the to-do list should be empty')
def step_then_todo_list_should_be_empty(context):
    assert not context.manager.list_tasks(), 'To-do list is not empty'
