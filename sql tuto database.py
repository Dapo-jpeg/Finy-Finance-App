#Import sqlite3
import sqlite3

#Initialize/setup database 
def get_connection(database_name):
    try:
        return sqlite3.connect(database_name)
    except Exception as e:
        print(f"Error {e}")
        raise

#Create a table 
def create_table(connection):
    query = """
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        email TEXT
        );
    """
    try:
        with connection:
            connection.execute(query)
        print("Table was created!")
    except Exception as e:
        print(e)

#Insert a transaction in the table
def insert_user(connection, name, age, email):
    query = """
    INSERT INTO users (name, age, email) VALUES (?, ?, ?);
    """

    try:
        with connection:
            connection.execute(query, (name, age, email))
        print(f"user: {name} has been added ")
    except Exception as e:
        print(e)


#query for all users
def fetch_users(connection, condition: str=None) -> list[tuple]: #(josh, 45, email)
    query = "SELECT * FROM users"
    if condition:
        query += f"WHERE {condition}"
    
    try:
        with connection:
            rows = connection.execute(query). fetchall()
        return rows
    except Exception as e:
        print(e)


#delete a user from the database
def delete_user(connection,user_id:int):
    query = "DELETE FROM users WHERE id = ?"
    try:
        with connection: 
            connection.execute(query,(user_id,))
        print(f"User ID: {user_id} has been deleted")
    except Exception as e:
        print(e)

#update a user
def update_user(connection,user_id:int, email:str):
    query = "UPDATE users SET email = ? WHERE id =?"

    try:
        with connection:
            connection.execute(query, (email, user_id))
        print(f"User id {user_id} has new email: {email}")

    except Exception as e:
        print (e)

# Bonus - Add multiple users at the same time
def insert_users(connection, users:list[tuple[str, int, str]]):
    query = "INSERT INTO users (name, age, email) VALUES (?,?,?)"

    try:
        with connection:
            connection.executemany(query, users)
        print(f" {len(users)} users were added to the database")

    except Exception as e:
        print(e)



# Main function calling everything
def main():
    connection = get_connection("sql trial.db")

    try: 
        #create my table
        create_table(connection)

        x = int(input("1. Activate | 2. Freeze"))
        while x!= 2:

            start = input("Enter option (Add, Delete, Update, Search, Add Many):").lower()
            if start == 'add':
                name = input("name= ")
                age = int(input("age= "))
                email = input("email= ")
                insert_user(connection, name, age, email)

            elif start == 'search':
                print ("All users:")
                for user in  fetch_users(connection): #you can add a condition if you want
                    print(user)

            elif start == 'delete':
                user_id = int(input("Input the number of the user you want to delete"))
                delete_user(connection, user_id)

            elif start == 'update':
                user_id = int(input("Enter the number of the user you want to update their email"))
                new_email = input("Enter the email you want to change to: ")
                update_user(connection, user_id, new_email)

            elif start == "add many":
                users = [("chandler", 29, "friends@none.com"),
                        ("mike", 32, "work@always.com"),
                        ("olga", 68, "siberiangrandma@gmail.com")] 
                insert_users(connection, users)

            x = int(input("1. Activate | 2. Freeze"))

    finally:
        connection.close()

if __name__ == '__main__':
    main()
