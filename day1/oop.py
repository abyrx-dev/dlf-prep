class Employee:
    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Salary: {self.salary}")

emp1 = Employee("Abinesh", "IT", 38000)
emp1.display()
emp2 = Employee("RAvi", "HR", 42000)
emp2.display()

emp3 = Employee("priya", "Finance", 35000)
emp3.display()

