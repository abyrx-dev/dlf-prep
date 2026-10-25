import sqlite3

conn = sqlite3.connect("company.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY,
        name TEXT,
        department TEXT,
        salary INTEGER
        )
    """)

conn.commit()
print("Database and table created!")
conn.close()
conn = sqlite3.connect("company.db")
cursor = conn.cursor()

cursor.execute("INSERT INTO employees (name, department, salary) VALUES ('Abinesh', 'IT', 38000)")
cursor.execute("INSERT INTO employees (name, department, salary) VALUES ('Ravi', 'HR', 42000)")
cursor.execute("INSERT INTO employees (name, department, salary) VALUES ('Priya', 'Finance', 35000)")

conn.commit()
print("Data inserted!")
conn.close()
conn = sqlite3.connect("company.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM employees")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()


conn = sqlite3.connect("company.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM employees WHERE department = 'IT'")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
conn = sqlite3.connect("company.db")
cursor = conn.cursor()

cursor.execute("UPDATE employees SET salary = 45000 WHERE name = 'Abinesh'")
conn.commit()

cursor.execute("SELECT * FROM employees")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
