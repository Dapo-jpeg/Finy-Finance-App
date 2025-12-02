import sqlite3

#Initializing database
def get_connection():
    try:
        connection = sqlite3.connect("data/finy.db")
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


def fetch_many_transactions():
    connection = get_connection()
    cursor = connection.cursor()

    query = "SELECT * FROM transactions"

    try: 
        rows = cursor.execute(query).fetchall()
        connection.commit()

        column_names = [description[0] for description in cursor.description]
        result_dict = [dict(zip(column_names, row)) for row in rows]
        return result_dict
    except Exception as e:
        print(e)
    finally:
        connection.close()

    
    pass


def fetch_many_recurring_expenses():
    connection = get_connection()
    cursor = connection.cursor()

    query = "SELECT * FROM recurring_expenses"
    try:
        rows = cursor.execute(query).fetchall()
        connection.commit()

        column_names = [description[0] for description in cursor.description]
        result_dict = [dict(zip(column_names, row)) for row in rows]
        return result_dict
    except Exception as e:
        print(e)
    finally:
        connection.close()

def fetch_to_show_all_recurring_expenses():
    connection = get_connection()
    cursor = connection.cursor()

    query = """SELECT id, recurring_expenses.name AS recurring_expense_name, amount, category, frequency, bank_accounts.name AS bank_account_name, recurring_expenses.bank_account_id AS bank_account_id, last_date_paid, next_pay_date FROM recurring_expenses
            JOIN bank_accounts ON recurring_expenses.bank_account_id = bank_accounts.bank_account_id"""
    try:
        rows = cursor.execute(query).fetchall()
        connection.commit()

        column_names = [description[0] for description in cursor.description]
        result_dict = [dict(zip(column_names, row)) for row in rows]
        return result_dict
    except Exception as e:
        print(e)
    finally:
        connection.close()

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

def insert_transaction(values):
    connection = get_connection()
    cursor = connection.cursor()

    query = "INSERT INTO transactions VALUES (:id, :date, :type, :category, :amount, :note, :bank_account_id)"

    try:
        cursor.execute(query, (values))
        connection.commit()
    except Exception as e :
        print(e)
    finally:
        connection.close()

def insert_many_transactions():
    #* will do later as a feature
    pass 

def insert_recurring_expense(values):
    connection = get_connection()
    cursor = connection.cursor()

    query = "INSERT INTO recurring_expenses VALUES (:id, :name, :last_date_paid, :type, :category, :amount, :frequency, :note, :bank_account_id, :next_pay_date)"

    try:
        cursor.execute(query, (values))
        connection.commit()
    except Exception as e :
        print(e)
    finally:
        connection.close()

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

def update_transaction(values):
    connection = get_connection()
    cursor = connection.cursor()

    query = "UPDATE transactions SET date= :date, type= :type, category= :category, amount= :amount, note= :note, bank_account_id= :bank_account_id WHERE id= :id"

    try:
        cursor.execute(query, (values))
        connection.commit()
    except Exception as e:
        print(e)
    finally:
        connection.close()

def update_recurring_expense(values):
    connection = get_connection()
    cursor = connection.cursor()

    query = "UPDATE recurring_expenses SET name=:name, last_date_paid= :last_date_paid, type= :type, category= :category, amount= :amount, frequency= :frequency, note= :note, bank_account_id= :bank_account_id, next_pay_date = :next_pay_date WHERE id= :id"

    try:
        cursor.execute(query, (values))
        connection.commit()
    except Exception as e:
        print(e)
    finally:
        connection.close()

#------------------------------------------------

#delete row in table
def delete_bank_account(bank_account_id):
    connection = get_connection()
    cursor = connection.cursor()

    query = "DELETE FROM bank_accounts WHERE bank_account_id = ?"

    try:
        cursor.execute(query, (bank_account_id,))
        connection.commit()
    except Exception as e:
        print(e)
    finally:
        connection.close()

def delete_transaction(transaction_id):
    connection = get_connection()
    cursor = connection.cursor()

    query= "DELETE FROM transactions WHERE id = ?"

    try: 
        cursor.execute(query, (transaction_id,))
        connection.commit()
    except Exception as e:
        print(e)
    finally:
        connection.close()

def delete_recurring_expense(recurring_expense_id):
    connection = get_connection()
    cursor = connection.cursor()

    query= "DELETE FROM recurring_expenses WHERE id = ?"

    try: 
        cursor.execute(query, (recurring_expense_id,))
        connection.commit()
    except Exception as e:
        print(e)
    finally:
        connection.close()

#------------------------------------------------

#Update the balances
def update_bank_balance(bank_account_id, net_balance):
    connection = get_connection()
    cursor = connection.cursor()

    query = "UPDATE bank_accounts SET balance = ? WHERE bank_account_id = ? "

    try:
        cursor.execute(query, (net_balance, bank_account_id))
        connection.commit()
    except Exception as e:
        print(e)
    finally:
        connection.close()

def update_last_date_paid():
    connection = get_connection()
    cursor = connection.cursor()

    query = ""

    try:
        cursor.execute(query)
        connection.commit()
    except Exception as e:
        print(e)
    finally:
        connection.close()

#------------------------------------------------

#analytics
def fetch_all_transaction_last_month():
    connection = get_connection()
    cursor = connection.cursor()

    query = "SELECT id, type, category, amount, bank_account_id FROM transactions WHERE date >= DATETIME ('now','-30 day')"

    try:
        rows = cursor.execute(query).fetchall()
        connection.commit()

        column_names = [description[0] for description in cursor.description]
        result_dict = [dict(zip(column_names, row)) for row in rows]
        return result_dict

    except Exception as e:
        print(e)

    finally:
        connection.close()

def fetch_month_transaction(year, month):
    connection = get_connection()
    cursor = connection.cursor()

    query = "SELECT type, SUM(amount) FROM transactions WHERE strftime('%Y', date) = ?  AND strftime('%m', date) =? GROUP BY type"

    try:
        rows = cursor.execute(query,(year, month)).fetchall()
        connection.commit()

        column_names = [description[0] for description in cursor.description]
        result_dict = [dict(zip(column_names, row)) for row in rows]

        return(result_dict)
    except Exception as e:
        print(e)

    finally:
        connection.close()