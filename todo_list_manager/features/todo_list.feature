Feature: To-Do List Management
  As a user
  I want to manage my to-do list
  So that I can keep track of my tasks

  Scenario: Add a task to the to-do list
    Given the to-do list is empty
    When the user adds a task "Buy groceries"
    Then the to-do list should contain "Buy groceries"

  Scenario: List all tasks in the to-do list
    Given the to-do list contains tasks:
      | Task         |
      | Buy groceries|
      | Pay bills    |
    When the user lists all tasks
    Then the output should contain:
      """
      Tasks:
      - Buy groceries
      - Pay bills
      """

  Scenario: Mark a task as completed
    Given the to-do list contains tasks:
      | Task         | Status  |
      | Buy groceries| Pending |
    When the user marks task "Buy groceries" as completed
    Then the to-do list should show task "Buy groceries" as completed

  Scenario: Edit a task in the to-do list
    Given the to-do list contains tasks:
      | Task         | Due Date | Priority |
      | Buy groceries| 2024-08-01 | High |
    When the user edits the task "Buy groceries" to have new name "Buy food" and new due date "2024-08-02"
    Then the to-do list should contain a task with name "Buy food" and due date "2024-08-02"

  Scenario: Clear the entire to-do list
    Given the to-do list contains tasks:
      | Task         |
      | Buy groceries|
      | Pay bills    |
    When the user clears the to-do list
    Then the to-do list should be empty
