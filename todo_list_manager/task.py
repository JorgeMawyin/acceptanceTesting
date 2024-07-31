class Task:
    def __init__(self, name, due_date=None, priority=None):
        self.name = name
        self.due_date = due_date
        self.priority = priority
        self.status = "Pending"

    def mark_as_completed(self):
        self.status = "Completed"

    def __str__(self):
        return f"{self.name} [Due: {self.due_date}, Priority: {self.priority}, Status: {self.status}]"
