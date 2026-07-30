import oracledb
import json
import traceback

from Emp_Mgmnt_V3.Emp_mgmnt_v3_DB import DB_Connection

_connection = None

def get_connection():
    global _connection

    if _connection is None:
        _connection = oracledb.connect(
            user='pub',
            password='p6bd5v',
            dsn="usws1devdb01.hrbl.net:1527/DMDEV"
        )
        print('DB connected successfully')
    # else:
    #     print("Reusing existing connection")
    return _connection

def get_cursor():
    conn = get_connection()
    return conn.cursor()

def get_commit():
    conn = get_connection()
    conn.commit()

def add_employee(employees_json):
    conn = get_connection()
    cur = conn.cursor()

    cur.callproc(
        "pkg_emp_data.add_employee",
        [
            json.dumps(employees_json)
        ]
    )
    conn.commit()

def delete_employee(emp_id):
    conn = get_connection()
    curr = conn.cursor()
    out_val = curr.var(str)
    res_params = curr.callproc(
        "pkg_emp_data.delete_employee",
        [
            emp_id,
            out_val
        ]
    )
    msg_from_db = res_params[1]
    print(msg_from_db)
    conn.commit()