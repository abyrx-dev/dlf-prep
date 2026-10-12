def employee_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

employee_info(name="Abinesh", role="python Developer", company="DLF")

def calculate_salary(base, *bonuses):
    total = base + sum(bonuses)
    print(f"Base: {base}")
    print(f"Bonuses: {bonuses}")
    print(f"Total Salary: {total}")

calculate_salary(30000, 5000, 2000, 1000)
def employee_report(name, department, salary, *skills):
    print(f"\n---Employee Report ---")
    print(f"Name: {name}")
    print(f"Department: {department}")
    print(f"salary: {salary}")
    print(f"Skills: {', '.join(skills)}")

employee_report("Abinesh", "IT", 38000, "python", "Git", "SQL")

          
    