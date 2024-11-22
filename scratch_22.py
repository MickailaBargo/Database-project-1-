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


    query = "SELECT * FROM pet WHERE species = 'dog' AND sex = 'f'"
    cursor.execute(query)


    print("Records of female dogs in the `pet` table:")
    column_headers = [desc[0] for desc in cursor.description]
    print(column_headers)
    for row in cursor.fetchall():
        print(row)

except mc.Error as err:
    print(f"Error: {err}")

finally:
    if 'cursor' in locals():
        cursor.close()
        print("Cursor closed.")
    if 'conn' in locals():
        print("Connection closed.")