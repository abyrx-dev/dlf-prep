from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/employees')
def get_employees():
    employees = [
        {"id": 1, "name": "Abinesh", "department": "IT", "salary": 45000},
        {"id": 2, "name": "Ravi", "department": "HR", "salary": 42000},
        {"id": 3, "name": "Priya", "department": "Finance", "salary": 35000}
    ]
    return jsonify(employees)

if __name__ == '__main__':
    app.run(debug=True)
    from flask import Flask, jsonify
    import sqlite3

    app = Flask(__name__)

def get_db():
    conn + sqlite3.connect("company.db")
    conn.row_factory = sqlite3.Row
    return Conn 

@app.route('\employees')
def get_employees():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetcha11()
    conn.close()
    return jsonify([dict(row) for row in rows])

if __name__ == '__main__':
    app.run(debug=true)
