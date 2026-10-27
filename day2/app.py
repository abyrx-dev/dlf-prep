from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect("company.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/employees')
def get_employees():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees")
    row = cursor.fetchall()
    conn.close()
    return jsonify([dict(row) for row in row])

@app.route('/employees', methods=['POST'])
def add_employee():
    data = request.get_json()
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO employees (name, department, salary) VALUES (?, ?, ?)",
                   (data['name'], data['department'], data['salary']))
    conn.commit()
    conn.close()
    return jsonify({"message": "Employee added!"}), 201

if __name__ == '__main__':
    app.run(debug=True)



                    