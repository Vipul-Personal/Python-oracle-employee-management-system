import json
from datetime import datetime
from employee_data import employees
from employee import Employee


def load_employees():
    employees.clear()
    try:
        with open('emp_mgmt_sys_json.json', 'r') as f:
            employees_json = json.load(f)

            for emp_data in employees_json:
                emp_data['joining_date'] = datetime.strptime(
                    emp_data['joining_date'], '%Y-%m-%d').date()

                employee = Employee(
                    emp_data['emp_id'],
                    emp_data['name'],
                    emp_data['dept'],
                    emp_data['sal'],
                    emp_data['joining_date']
                )
                employees.append(employee)


    except FileNotFoundError:
        print("The file wasn't found.")
    except Exception as e:
        print(f"Invalid input: {e}")