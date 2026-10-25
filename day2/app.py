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
    