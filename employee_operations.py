import json
from employee import Employee
from employee_data import employees
from datetime import datetime
import employee_repository


def save_employees():
    try:
        employees_json = []

        for emp in employees:
            emp_data = {
                'emp_id': emp.emp_id,
                'name': emp.emp_name,
                'dept': emp.emp_dept,
                'sal': emp.emp_sal,
                'joining_date': emp.emp_doj.strftime('%Y-%m-%d')
            }

            employees_json.append(emp_data)

        # with open('emp_mgmt_sys_json.json', 'w') as f:
        #     json.dump(employees_json, f, indent=4)

        employee_repository.add_employee(employees_json)

    except Exception as e:
        print(f"Invalid input: {e}")


def get_employee_by_id(emp_id):
    try:
        if emp_id <= 0:
            return None
        else:
            # for employee in employees:
            #     if employee.emp_id == emp_id:
            #         return employee
            search_emp_db(emp_id)

            return None

    except Exception as e:
        print(f"Invalid input: {e}")
        return


def validate_employee(emp_id=None,
                      emp_name=None,
                      emp_sal=None,
                      emp_dept=None,
                      emp_doj=None,
                      is_update=False
                      ):
    try:
        if emp_id is not None:

            if not emp_id.strip():
                print("EMPLOYEE ID cannot be empty")
                return False

            try:
                emp_id = int(emp_id)
            except ValueError:
                print("EMPLOYEE ID must be numeric")
                return False

            if emp_id <= 0:
                print("EMPLOYEE ID cannot be zero or negative")
                return False

            if any(emp.emp_id == emp_id for emp in employees) and not is_update:
                print("Employee ID already exists")
                return False

        if emp_name is not None:
            if not emp_name.strip():
                print("EMPLOYEE NAME cannot be empty")
                return False

        if emp_sal is not None:
            try:
                emp_sal = float(emp_sal)
            except ValueError:
                print("Salary must be numeric")
                return False

            if emp_sal <= 0:
                print("INVALID EMPLOYEE SAL")
                return False

        if emp_dept is not None:
            if not emp_dept.strip():
                print("EMPLOYEE DEPT cannot be empty")
                return False

        if emp_doj is not None:
            if emp_doj > datetime.now().date():
                print("EMPLOYEE DOJ cannot be future date")
                return False

        return True

    except Exception as e:
        print(f"Invalid input: {e}")
        return False


def add_emp():
    try:
        global employees
        is_valid = None
        emp_name = None
        emp_sal = None
        emp_dept = None
        emp_join_date = None

        no_emp = int(input('How many employees data you want to add?: '))

        for _ in range(no_emp):
            emp_id = input('Enter employee id: ')
            emp_name = input('Enter employee name: ')
            emp_dept = input('Enter employee department: ')
            emp_sal = input('Enter employee salary: ')
            emp_join_date = input('Enter employee joining date (DD-MM-YYYY): ')

            try:
                joining_date = datetime.strptime(emp_join_date, '%d-%m-%Y').date()
            except ValueError:
                print("Invalid date, try again later")
                continue

            is_valid = validate_employee(emp_id,
                                         emp_name,
                                         emp_sal,
                                         emp_dept,
                                         joining_date)

            if not is_valid:
                continue

            emp_id = int(emp_id)
            emp_sal = float(emp_sal)

            employee = Employee(emp_id,
                                emp_name,
                                emp_dept,
                                emp_sal,
                                joining_date)
            employees.append(employee)

        save_employees()
        print("Employee added successfully")
        search_emp()

    except Exception as e:
        print(f"Invalid input: {e}")
        return


def search_emp(emp_id=0,
               emp_name='all',
               emp_dept='all', ):
    try:
        found = False

        if not employees:
            print("No employees found")
        elif emp_id == 0 and emp_name == 'all' and emp_dept == 'all':
            print("\nEmployee Records:")
            found = True

            for emp in employees:
                emp.display()

        else:
            for employee in employees:
                if employee.emp_id == emp_id:
                    found = True
                    employee.display()
                    break

                elif employee.emp_name.lower() == emp_name:
                    found = True
                    employee.display()

                elif employee.emp_dept.lower() == emp_dept:
                    found = True
                    employee.display()

            if not found:
                print('No employee found')
    except Exception as e:
        print(f"Invalid input: {e}")
        return


def search_emp_db(emp_id=0,
                  emp_name='all',
                  emp_dept='all', ):
    try:
        employees = []
        curr = employee_repository.get_cursor()
        if emp_id == 0:
            curr.execute("""select emp_id   ID,
                                   emp_name Name,
                                   emp_dept Dept,
                                   emp_sal  Sal,
                                   emp_doj  DOJ
                            from EMPLOYEE""")
        else:
            curr.execute('select * from EMPLOYEE where nvl(emp_id,0) = :empid', empid=emp_id)
        result = curr.fetchall()
        row_cnt = len(result)
        if not result:
            print("No employee record present")
        else:
            for row in result:
                emp = Employee(
                    row[0],
                    row[1],
                    row[2],
                    row[3],
                    row[4],

                )
                employees.append(emp)

                for emp in employees:
                    emp.display()

    except Exception as e:
        print(f"Invalid input: {e}")
        return


def show_emp_dtls(action: int = 0):
    try:
        found = False
        # '7': 'View all Employee ID',
        # '8': 'View all Employee name',
        # '9': 'View all Dept details'
        if not employees:
            print("No employees found")
        elif action == 7:
            print("\nEmployee Records:")
            found = True
            names = [emp.display_emp_id() for emp in employees]


        elif action == 8:
            print("\nEmployee Records:")
            found = True
            names = [emp.display_emp_name() for emp in employees]

        elif action == 9:
            print("\nEmployee Records:")
            found = True
            names = [emp.display_emp_dept() for emp in employees]

            if not found:
                print('No employee found')
    except Exception as e:
        print(f"Invalid input: {e}")
        return


def upd_emp(emp_id,
            new_name=None,
            new_dept=None,
            new_salary=None,
            new_join_date=None):
    try:
        found = False

        for employee in employees:

            if employee.emp_id == emp_id:
                found = True

                is_valid = validate_employee(emp_name=new_name,
                                             emp_sal=new_salary,
                                             emp_dept=new_dept,
                                             emp_doj=new_join_date,
                                             is_update=True)

                if not is_valid:
                    continue

                if new_name is not None:
                    employee.emp_name = new_name

                if new_dept is not None:
                    employee.emp_dept = new_dept

                if new_salary is not None:
                    employee.emp_sal = new_salary

                if new_join_date is not None:
                    employee.emp_doj = new_join_date

                save_employees()

                print("Employee updated successfully")
                employee.display()
                break

        if not found:
            print('No employee found')
    except Exception as e:
        print(f"Invalid input: {e}")
        return


######### handle_search() ##############
def handle_search():
    try:
        search_options = {
            '1': 'Employee ID, Give 0 for all employees',
            '2': 'Employee Name Give ALL for all employees',
            '3': 'Employee Department  Give ALL for all employees',
            '4': 'Employee salary greater than ..',
            '5': 'Employee belongs to department ..',
        }

        for key, value in search_options.items():
            print(f"{key}: {value}")

        search_action = int(input('What you want to do? Choose an option: '))
        search_emp_id = 0
        search_emp_name = 'all'
        search_emp_dept = 'all'
        search_emp_sal = 0

        if search_action == 1:
            search_emp_id = int(input('Enter employee id: '))
        elif search_action == 2:
            search_emp_name = input('Enter employee name: ').lower()
        elif search_action == 3:
            search_emp_dept = input('Enter employee dept: ').lower()
        elif search_action == 4:
            search_emp_sal = float(input('Enter salary: '))
            result = [
                emp
                for emp in employees
                if emp.emp_sal > search_emp_sal
            ]
            # for emp in result:
            if not result:
                print("No employee found")
            else:
                for emp in result:
                    emp.display_emp_filter_dtls()

            return
        elif search_action == 5:
            search_emp_dept = input('Enter dept: ').lower()
            result = [
                emp
                for emp in employees
                if emp.emp_dept == search_emp_dept
            ]
            # for emp in result:
            if not result:
                print('No record found')
            else:
                for emp in result:
                    emp.display_emp_filter_dtls()
            return

        search_emp_db(emp_id=search_emp_id,
                      emp_name=search_emp_name,
                      emp_dept=search_emp_dept)


    except Exception as e:
        print(f"Invalid input: {e}")
        return


######### handle_upd() ##############
def handle_upd():
    try:
        upd_emp_menu = {
            '1': 'Update employee name',
            '2': 'Update employee dept',
            '3': 'Update employee salary',
            '4': 'Update employee joining date'
        }

        upd_emp_id = None
        emp_new_name = None
        emp_new_dept = None
        emp_new_salary = None
        emp_new_join_date = None

        upd_emp_id = int(input('Enter employee id: '))

        if upd_emp_id <= 0:
            print('Employee id is invalid')
        else:
            for key, value in upd_emp_menu.items():
                print(f"{key}: {value}")
            upd_action = int(input('What you want to update? Choose an option: '))
            if upd_action == 1:
                emp_new_name = input('Enter new name: ')
            elif upd_action == 2:
                emp_new_dept = input('Enter new dept: ')
            elif upd_action == 3:
                emp_new_salary = float(input('Enter new salary: '))
            elif upd_action == 4:
                try:
                    emp_new_join_date = datetime.strptime(
                        input('Enter new joining date (DD-MM-YYYY): '),
                        '%d-%m-%Y'
                    ).date()
                except ValueError:
                    print("Invalid date")
                    return
            else:
                print('Invalid option. Please choose 1-4.')
                return
            upd_emp(emp_id=upd_emp_id,
                    new_name=emp_new_name,
                    new_dept=emp_new_dept,
                    new_salary=emp_new_salary,
                    new_join_date=emp_new_join_date)

    except Exception as e:
        print(f"Invalid input: {e}")
        return


def del_emp(emp_Id):
    try:
        del_action = None
        del_action = input('Do you want to delete employee? (y/n): ').lower()

        if del_action == 'y':
            # employees.remove(del_emp_id)
            employee_repository.delete_employee(emp_Id)
            print(f'Employee Id - {emp_Id}, deleted')
        elif del_action == 'n':
            print(f'As per request, Employee Id - {emp_Id}, not deleted')
        elif del_action not in ('n', 'y'):
            print("Invalid option. Please choose 'y' or 'n'")
            return
            # save_employees()
        search_emp()
    except Exception as e:
        print(f"Invalid input: {e}")
