with open("employees.txt", "w") as f:
    f.write("Abinesh,IT,38000\n")
    f.write("Ravi,HR,42000\n")
    f.write("priya,finance,35000\n")

    print("fille written successfully")
# Read from file
with open("employees.txt", "r") as f:
    content = f.read()
    print(content)
    