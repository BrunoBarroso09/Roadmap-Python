import mysql.connector


class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email

class UserRepository:

    def __init__(self, connection):
        self.connection = connection

    def insert_user(self, user: User):

        cursor = self.connection.cursor()
        query = "INSERT INTO User (name, email) VALUES (%s, %s)"
        cursor.execute(query, (user.name, user.email))

        self.connection.commit()
        cursor.close()
        print(f"User {user.name} was created!")

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