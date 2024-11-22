import MySQLdb as mc

try:
    conn = mc.connect(
        host="localhost",
        user="root",
        passwd="A20m96Ci%",
        db="menagerie"
    )
    print("Connected to the menagerie database!")

    cursor = conn.cursor()

    cursor.execute("DESCRIBE pet")
    print("Structure of the `pet` table:")
    for row in cursor.fetchall():
        print(row)

except mc.Error as err:
    print(f"Error: {err}")

finally:
    if 'cursor' in locals():
        cursor.close()
        print("Cursor closed.")
    if 'conn' in locals():
        conn.close()
        print("Connection closed.")
