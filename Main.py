import sqlite3

# Connect to database
conn = sqlite3.connect("employee.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    department TEXT,
    salary INTEGER
)
""")
conn.commit()

def add_employee():
    name = input("Enter name: ")
    department = input("Enter department: ")
    salary = int(input("Enter salary: "))
    cursor.execute(
        "INSERT INTO employees (name, department, salary) VALUES (?, ?, ?)",
        (name, department, salary)
    )
    conn.commit()
    print("Employee added successfully")

def view_employees():
    cursor.execute("SELECT * FROM employees")
    records = cursor.fetchall()
    for row in records:
        print(row)

def update_employee():
    emp_id = int(input("Enter employee ID to update: "))
    salary = int(input("Enter new salary: "))
    cursor.execute(
        "UPDATE employees SET salary = ? WHERE id = ?",
        (salary, emp_id)
    )
    conn.commit()
    print("Employee updated successfully")

def delete_employee():
    emp_id = int(input("Enter employee ID to delete: "))
    cursor.execute("DELETE FROM employees WHERE id = ?", (emp_id,))
    conn.commit()
    print("Employee deleted successfully")

def search_employee():
    emp_id = int(input("Enter employee ID to search: "))
    cursor.execute("SELECT * FROM employees WHERE id = ?", (emp_id,))
    record = cursor.fetchone()
    print(record if record else "Employee not found")

while True:
    print("\nEmployee Management System")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Search Employee")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        view_employees()
    elif choice == "3":
        update_employee()
    elif choice == "4":
        delete_employee()
    elif choice == "5":
        search_employee()
    elif choice == "6":
        break
    else:
        print("Invalid choice")

conn.close()
