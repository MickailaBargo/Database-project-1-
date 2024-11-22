
import MySQLdb as mc

try:
    conn = mc.connect(
        host='localhost',
        user='root',
        passwd='A20m96Ci%',
        db='pythonSQL'
    )
    print("Connection successful!")

    # Create a cursor
    cursor = conn.cursor()
    print("Cursor ready to perform operations!")

    # Execute the SQL command to list all databases
    cursor.execute("SHOW DATABASES")

    # Fetch and display the databases
    print("Databases on the MySQL server:")
    for db in cursor.fetchall():
        print(db[0])

except mc.Error as err:

    print(f"Error: {err}")

finally:

    if 'cursor' in locals():
        cursor.close()
        print("Cursor closed.")
    if 'conn' in locals():
        conn.close()
        print("Connection closed.")

