from db import conn


def query(qry_statement='', args: None = None):
    cursor = conn.cursor()
    try:
        if args is None:
            cursor.execute(qry_statement)
        else:
            cursor.execute(qry_statement, args)
        return cursor.fetchall()
    except Exception as e:
        print(e)
        # throw error to handler
        raise e
    finally:
        cursor.close()
