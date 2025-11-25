from services import database
from models import account
import uuid

#Function to print all bank account data for updating
def print_all_account():
    return database.fetch_many_bank_accounts()

# function for adding an account to csv
def add_bank_account(account_input):
    #Add unique uuid
    account_input['bank_account_id'] = str(uuid.uuid4())
    #Validate data and create object
    #Creating object
    account_object = account.account(**account_input)
    #converting object to dict 
    account_input_data = {
        "name" : account_object.name, 
        "currency": account_object.currency,
        "balance": account_object.balance, 
        "account_type": account_object.account_type, 
        "starting_balance": account_object.starting_balance, 
        "note": account_object.note,
        "bank_account_id": account_object.bank_account_id
    }
    #pass data to database.py
    database.insert_bank_account(account_input_data)

#function for updating account.csv
def update_account(bank_account_id, field_to_change, new_value):
    accounts = database.fetch_many_bank_accounts()

    for account in accounts:
        if account['bank_account_id'] == bank_account_id:
            print("Account confirmed, updating...")

            if field_to_change not in ["name", "currency", "account_type", "starting_balance", "note"]:
                print("Invalid field name")
                return

            if field_to_change == "starting_balance":
                if int(new_value) < 0:
                    print("Invalid value. Amount must be greater than 0")
                    return
            
            account[field_to_change] = new_value
            database.update_bank_account(account)
            break

#function for removing account.csv
def remove_account(bank_account_id):
    accounts = database.fetch_many_bank_accounts()

    for account in accounts:
        if account['bank_account_id'] == bank_account_id:
            print("Account confirmed, deleteing...")

    database.delete_bank_account(bank_account_id)