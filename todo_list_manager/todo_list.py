from task import Task

class ToDoListManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, due_date=None, priority=None):
        task = Task(name, due_date, priority)
        self.tasks.append(task)

    def list_tasks(self):
        return self.tasks

    def mark_task_as_completed(self, name):
        for task in self.tasks:
            if task.name == name:
                task.mark_as_completed()
                return True
        return False

    def edit_task(self, old_name, new_name=None, new_due_date=None, new_priority=None):
        for task in self.tasks:
            if task.name == old_name:
                if new_name:
                    task.name = new_name
                if new_due_date:
                    task.due_date = new_due_date
                if new_priority:
                    task.priority = new_priority
                return True
        return False

    def clear_tasks(self):
        self.tasks = []

if __name__ == "__main__":
    manager = ToDoListManager()
    
    while True:
        print("\nTo-Do List Manager")
        print("1. Add task")
        print("2. List tasks")
        print("3. Mark task as completed")
        print("4. Clear tasks")
        print("5. Edit task")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            name = input("Task name: ")
            due_date = input("Due date (optional): ")
            priority = input("Priority (optional): ")
            manager.add_task(name, due_date, priority)
            print(f'Task "{name}" added.')
        
        elif choice == '2':
            tasks = manager.list_tasks()
            if tasks:
                print("\nTasks:")
                for task in tasks:
                    print(task)
            else:
                print("No tasks found.")
        
        elif choice == '3':
            name = input("Task name to mark as completed: ")
            if manager.mark_task_as_completed(name):
                print(f'Task "{name}" marked as completed.')
            else:
                print(f'Task "{name}" not found.')
        
        elif choice == '4':
            manager.clear_tasks()
            print("All tasks cleared.")
        
        elif choice == '5':
            name = input("Task name to edit: ")
            new_name = input("New name (leave blank to keep current): ")
            new_due_date = input("New due date (leave blank to keep current): ")
            new_priority = input("New priority (leave blank to keep current): ")
            if manager.edit_task(name, new_name, new_due_date, new_priority):
                print(f'Task "{name}" updated.')
            else:
                print(f'Task "{name}" not found.')
        
        elif choice == '6':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")