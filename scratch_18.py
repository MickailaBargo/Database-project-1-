
import MySQLdb as mc

try:

    conn = mc.connect(
        host="localhost",
        user="root",
        passwd="A20m96Ci%"
    )
    print("Connection successful!")


    cursor = conn.cursor()


    cursor.execute("DROP DATABASE IF EXISTS menagerie")
    print("Database 'menagerie' dropped successfully (if it existed).")

except mc.Error as err:

    print(f"Error: {err}")

finally:

    if 'cursor' in locals():
        cursor.close()
        print("Cursor closed.")
    if 'conn' in locals():
        conn.close()
        print("Connection closed.")
