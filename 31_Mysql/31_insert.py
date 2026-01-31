import mysql.connector
from Core.identifier import GenerateUUID
from mysql.connector import errorcode


class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email

class UserRepository:

    def __init__(self, connection):
        self.connection = connection

    def insert_user(self, user: User):
        generate_uuid = GenerateUUID.v5(user.email)
        cursor = self.connection.cursor()
        query = "INSERT INTO User (id, name, email) VALUES (%s, %s, %s)"

        try:
            cursor.execute(query,(generate_uuid, user.name, user.email))
            self.connection.commit()
            print(f"User {user.name} was created!")
        except mysql.connector.Error as err:
            # O código 1062 é o padrão do MySQL para "Duplicate entry"
            if err.errno == errorcode.ER_DUP_ENTRY:
                print(f"⚠️ Error: This user with this email '{user.email}' already exist in the database (Duplicate Id).\n")
            else:
                print(f"❌ Error occurred: {err}")
        finally:
            cursor.close()

    def get_all_users(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM User")
        users = cursor.fetchall()
        cursor.close()

        for user in users:
            print(f"id: {user[0]} | name: {user[1]} | email: {user[2]}")

# 1. Create connection
conn = mysql.connector.connect(host="localhost", user="root", password="root", database="python")

# 2. Create repository
repo = UserRepository(conn)

# 3. Create users
users = [
    User("Jane", "jane@gmail.com"),
    User("Peter", "peter@gmail.com")
]

# 4. Save all user using same connection
for user in users:
    repo.insert_user(user)

repo.get_all_users()

conn.close()