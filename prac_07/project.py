import datetime

class Project:
    def __init__(self, name, start_date, priority, estimate, completion):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.estimate = estimate
        self.completion = completion

    def update(self, new_completion=None, new_priority=None):
        if new_completion is not None:
            self.completion = new_completion
        if new_priority is not None:
            self.priority = new_priority

    def __str__(self):
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, estimate: ${self.estimate:.2f}, completion: {self.completion}%"

    def is_vintage(self):
        current_year = datetime.datetime.now().year
        return current_year - self.start_date.year >= 50