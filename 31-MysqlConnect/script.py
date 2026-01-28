import mysql.connector

try:
    connect = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
    )

    if connect.is_connected():
        cursor = connect.cursor()
        cursor.execute("SHOW DATABASES")
        results = cursor.fetchall()
        for database in results:
            print(database)

except mysql.connector.Error as e:
    print(f"Error: {e}")