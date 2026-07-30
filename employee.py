
class Employee:
    def __init__(self,
                 emp_id,
                 emp_name,
                 emp_dept,
                 emp_sal,
                 emp_doj):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_dept = emp_dept
        self.emp_sal = emp_sal
        self.emp_doj = emp_doj

    def display(self):
        print(f'Id - {self.emp_id}, '
              f'Name - {self.emp_name}, '
              f'Dept - {self.emp_dept}, '
              f'Salary - {self.emp_sal}, '
              f'DOJ - {self.emp_doj.strftime('%d-%m-%Y')}'
              )

    def display_emp_name(self):
        print(f'Name - {self.emp_name}')

    def display_emp_id(self):
        print(f'ID - {self.emp_id}')

    def display_emp_dept(self):
        print(f'ID - {self.emp_dept}')

    def display_emp_filter_dtls(self):
        print(f'Id - {self.emp_id}, '
              f'Name - {self.emp_name}, '
              f'Dept - {self.emp_dept}, '
              f'Salary - {self.emp_sal} '
              )