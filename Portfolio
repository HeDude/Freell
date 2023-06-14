class Portfolio:
    def __init__(self, student):
        self.student = student
        self.entries = []

    def add_entry(self, entry):
        self.entries.append(entry)

    def get_entries(self):
        return self.entries

class Entry:
    def __init__(self, description, document):
        self.description = description
        self.document = document

class Student:
    def __init__(self, name):
        self.name = name
        self.portfolio = Portfolio(self)

    def add_portfolio_entry(self, description, document):
        entry = Entry(description, document)
        self.portfolio.add_entry(entry)

    def get_portfolio_entries(self):
        return self.portfolio.get_entries()

# Example usage
student = Student("John Doe")
student.add_portfolio_entry("Math assignment", "math_assignment.pdf")
entries = student.get_portfolio_entries()

for entry in entries:
    print(f"Description: {entry.description}, Document: {entry.document}")
