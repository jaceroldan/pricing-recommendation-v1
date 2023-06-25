from db import conn


def query(qry_statement=''):
    cursor = conn.cursor()
    try:
        cursor.execute(qry_statement)
        return cursor.fetchall()
    except Exception as e:
        print(e)
        # throw error to handler
        raise e
    finally:
        cursor.close()
