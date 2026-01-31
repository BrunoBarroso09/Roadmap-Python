import mysql.connector

try:
    connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="python"
    )

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM User")
    users = cursor.fetchall()
    for user in users:
        print(f"id: {user[0]} | name: {user[1]} | email: {user[2]}")

    cursor.close()
    connection.close()

except mysql.connector.Error as e:
    print(f"Error: {e}")