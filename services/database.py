import sqlite3

#Initializing database
def get_connection():
    try:
        connection = sqlite3.connect("finy.db")
        connection.execute("PRAGMA foreign_keys = ON;")
        return connection
    except Exception as e:
        print(e)

#Creates tables
def create_tables():
    connection = get_connection()
    cursor = connection.cursor()

    try:
        #create bank account table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS bank_accounts(
            bank_account_id TEXT PRIMARY KEY, 
            name TEXT,
            currency TEXT,
            account_type TEXT,
            starting_balance REAL,
            note TEXT
            );
        """)
        
        #create transactions
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions(
            id TEXT PRIMARY KEY,
            date TEXT,
            type TEXT, 
            category TEXT, 
            amount REAL,
            note TEXT,
            bank_account_id TEXT,
            FOREIGN KEY (bank_account_id) REFERENCES bank_accounts(bank_account_id)
            );
        """)
        
        #create recurring_expenses
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS recurring_expenses (
            id TEXT PRIMARY KEY, 
            name TEXT,
            date TEXT,
            type TEXT,
            category TEXT,
            amount REAL, 
            frequency TEXT, 
            note TEXT, 
            bank_account_id TEXT,
            FOREIGN KEY (bank_account_id) REFERENCES bank_accounts (bank_account_id)
            );
        """)

        connection.commit()
        #! remove later
        print("Successflully created tables")
    except Exception as e:
        print(e)
    finally:
        connection.close()

    #create transaction table:

    #create recurring_expenses table:

#-------------------------------------------------

#Fetching data to read
def fetch_one_bank_account():
    pass


def fetch_many_bank_accounts():
    connection = get_connection()
    cursor= connection.cursor()

    try:
        query = "SELECT * FROM bank_accounts"
        
        rows = cursor.execute(query).fetchall()
        connection.commit()
        
        #Getting column names so I can convert to list of dictionaries
        column_names = [description[0] for description in cursor.description]

        #creating a list of dictionaries and zipping the column name with the row
        result_dict = [dict(zip(column_names, row)) for row in rows]
        return result_dict
    except Exception as e:
        print(e)
    finally:
        connection.close()


def fetch_one_transaction():
    pass

def fetch_many_transactions():
    pass

def fetch_one_recurring_expense():
    pass

def fetch_many_recurring_expenses():
    pass

#----------------------------------------------

#Insert into table
def insert_bank_account(values):
    connection = get_connection()
    cursor = connection.cursor()
    try:
        query = "INSERT INTO bank_accounts (bank_account_id, name, currency, account_type, starting_balance, note) VALUES (:bank_account_id, :name, :currency, :account_type, :starting_balance, :note) "
        cursor.execute(query, (values))
        connection.commit()
        print(f"{values} have been added!")
    except Exception as e:
        print(e)
    finally:
        connection.close()
    pass

def insert_transaction():
    pass

def insert_many_transactions():
    #* will do later as a feature
    pass 

def insert_recurring_expense():
    pass

def insert_many_recurring_expenses():
    #* will do later as a feature
    pass

#----------------------------------------------

#update row in table
def update_bank_account(values):
    connection = get_connection()
    cursor = connection.cursor()
    try: 
        query = "UPDATE bank_accounts SET name = :name, currency = :currency, account_type = :account_type, starting_balance = :starting_balance, note = :note WHERE bank_account_id=:bank_account_id"
        cursor.execute(query, (values))
        connection.commit()
    except Exception as e:
        print(e)
    finally:
        connection.close()

def update_transaction():
    pass

def update_recurring_expense():
    pass

#------------------------------------------------

#delete row in table
def delete_bank_account(bank_account_id):
    connection = get_connection()
    cursor = connection.cursor()

    query = "DELETE FROM bank_accounts WHERE bank_account_id = ?"

    try:
        cursor.execute(query, (bank_account_id,))
        connection.commit()
        pass
    except Exception as e:
        print(e)
    finally:
        connection.close()

    pass

def delete_transaction():
    pass

def delete_recurring_expense():
    pass