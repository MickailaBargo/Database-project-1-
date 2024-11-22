import MySQLdb as mc

try:

    conn = mc.connect(
        host="localhost",       #
        user="root",
        passwd="A20m96Ci%",
        db="menagerie"
    )
    print("Connected to the menagerie database!")


    cursor = conn.cursor()


    insert_query = """
    INSERT INTO pet (name, owner, species, sex, birth, death) VALUES
    ('Fluffy', 'Harold', 'cat', 'f', '1993-02-04', NULL),
    ('Claws', 'Gwen', 'cat', 'm', '1994-03-17', NULL),
    ('Buffy', 'Harold', 'dog', 'f', '1989-05-13', NULL),
    ('Fang', 'Benny', 'dog', 'm', '1990-08-27', NULL),
    ('Bowser', 'Diane', 'dog', 'm', '1989-08-31', '1995-07-29'),
    ('Chirpy', 'Gwen', 'bird', 'f', '1998-09-11', NULL),
    ('Whistler', 'Gwen', 'bird', NULL, '1997-12-09', NULL),
    ('Slim', 'Benny', 'snake', 'm', '1996-04-29', NULL),
    ('Puffball', 'Diane', 'hamster', 'f', '1999-03-30', NULL);
    """
    cursor.execute(insert_query)
    conn.commit()
    print("Data inserted successfully into the `pet` table!")

except mc.Error as err:

    print(f"Error: {err}")

finally:

    if 'cursor' in locals():
        cursor.close()
        print("Cursor closed.")
    if 'conn' in locals():
        conn.close()
        print("Connection closed.")
