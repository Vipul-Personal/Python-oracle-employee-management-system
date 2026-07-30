from DB_Connection import get_connection
import traceback

try:
    conn = get_connection()
    curr = conn.cursor()
    curr.execute('select * from dual')
    data = curr.fetchone()
    print(data[0])
except Exception as e:
    print(e)
    traceback.print_exc()