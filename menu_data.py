import employee_operations
import filter_function
from employee import Employee
import employee_repository

def menu():
    try:
        while True:
            menu_options = {
                '1': 'Add Employee',
                '2': 'View Employee details',
                '3': 'Search Employee',
                '4': 'Update Employee',
                '5': 'Delete Employee',
                '6': 'Exit',
                '7': 'View all Employee ID',
                '8': 'View all Employee name',
                '9': 'View all Dept details',
                '10': 'Filter data',
            }

            print('\nMenu')
            for key, value in menu_options.items():
                print(f"{key}: {value}")

            action = input('What you want to do? Choose an option: ')

            if action == '1':
                print(menu_options.get(action, action))
                employee_operations.add_emp()
            elif action == '2':
                print(menu_options.get(action, action))
                # employee_operations.search_emp()
                employee_operations.search_emp_db()
            elif action == '3':
                print(menu_options.get(action, action))
                employee_operations.handle_search()
            elif action == '4':
                print(menu_options.get(action, action))
                employee_operations.handle_upd()
            elif action == '5':
                print(menu_options.get(action, action))
                emp_id = None
                emp_id = int(input('Enter employee id: '))
                employee_operations.del_emp(emp_id)
                # employee_repository.delete_employee(emp_id)
            elif action == '6':
                return
            elif action == '7':
                print(menu_options.get(action, action))
                employee_operations.show_emp_dtls(7)
            elif action == '8':
                print(menu_options.get(action, action))
                employee_operations.show_emp_dtls(8)
            elif action == '9':
                print(menu_options.get(action, action))
                employee_operations.show_emp_dtls(9)
            elif action == '10':
                print(menu_options.get(action, action))
                filter_function.salary_more_than(99)
            else:
                print("Invalid option. Please choose 1-10.")

    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"Exception : {e}")
