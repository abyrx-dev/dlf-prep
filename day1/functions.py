def employee_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

employee_info(name="Abinesh", role="python Developer", company="DLF")