import MySQLdb as mc  # Or use mysql.connector if needed

try:
    # Connect to the MySQL server
    conn = mc.connect(
        host="localhost",       # MySQL host
        user="root",            # MySQL username
        passwd="A20m96Ci%", # Replace with your MySQL password
        db="menagerie"          # Database name
    )
    print("Connected to the menagerie database!")

    # Create a cursor object
    cursor = conn.cursor()

    # Query to retrieve name, birth, and month of birth
    query = "SELECT name, birth, MONTH(birth) AS `MONTH(birth)` FROM pet"
    cursor.execute(query)

    # Fetch and display the records
    print("`name`, `birth`, and `MONTH(birth)` columns from the `pet` table:")
    column_headers = [desc[0] for desc in cursor.description]
    print(column_headers)  # Print column headers for reference
    for row in cursor.fetchall():
        print(row)

except mc.Error as err:
    # Handle any errors
    print(f"Error: {err}")

finally:
    # Safely close the cursor and connection
    if 'cursor' in locals():
        cursor.close()
        print("Cursor closed.")
    if 'conn' in locals():
        conn.close()
        print("Connection closed.")
