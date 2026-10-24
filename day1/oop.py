class Employee:
    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Salary: {self.salary}")
    def give_raise(self, amount):
        self.salary += amount
        print(F"{self.name} new salay: {self.salary}")

emp1 = Employee("Abinesh", "IT", 38000)
emp1.display()
emp2 = Employee("RAvi", "HR", 42000)
emp2.display()
emp3 = Employee("priya", "Finance", 35000)
emp3.display()
emp1.give_raise(5000)


class Manager(Employee):
    def __init__(self, name, department, salary, team_size):
        super().__init__(name, department, salary)
        self.team_size = team_size

    def display_manager(self):
        self.display()
        print(f"Team Size: {self.team_size}")

mgr1 = Manager("suresh", "IT", 75000, 10)
mgr1.display_manager()


