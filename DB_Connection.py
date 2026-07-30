import oracledb

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
    # return conn.commit()