employees = ["Abinesh", "Ravi", "Priya", "Kumar", "Divya"]

print(employees[0])
print(employees[-1])
print(employees[1:3])
print(len(employees))
employee = {
    "name": "Abinesh",
    "department": "IT",
    "salary": 38000,
    "skills": ["Python", "Git", "SQL"]
}

print(employee["name"])
print(employee["skills"])
print(employee.get("department"))
employees_list = [
    {"name": "Abinesh", "salary": 38000},
    {"name": "Ravi", "salary": 42000},
    {"name": "Priya", "salary": 35000},
    {"name": "Kumar", "salary": 50000},
]

for emp in employees_list:
    print(f"{emp['name']} earns {emp['salary']}")
    