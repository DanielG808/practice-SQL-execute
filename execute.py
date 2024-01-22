import sqlite3

connection = sqlite3.connect('practice.db')

crsr = connection.cursor()


def execute(query, *args, fetchall=False):
    connection = sqlite3.connect('practice.db')
    cursor = connection.cursor()

    try:
        cursor.execute(query, args)
    
        connection.commit()

        if fetchall:
            results = cursor.fetchall()
            return results
    
    except sqlite3.Error as error:
        print(f"Error executing query: {error}")
    
    finally:
        cursor.close()
        connection.close()
    
    
