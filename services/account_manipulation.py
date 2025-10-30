from services import database
from models import account
import uuid

#Function to print all bank account data for updating
def print_all_account():
    return database.read_bank_account()

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
    database.write_bank_account(account_input_data)

#function for updating account.csv
def update_account(bank_account_id, field_to_change, new_value):
    accounts = database.read_bank_account()

    for account in accounts:
        if account['bank_account_id'] == bank_account_id:
            print("Transaction found, updating...")

            if field_to_change not in ["name", "currency", "account_type", "starting_balance", "note"]:
                print("Invalid field name")
                return

            if field_to_change == "starting_balance":
                if int(new_value) < 0:
                    print("Invalid value. Amount must be greater than 0")
                    return
            
            account[field_to_change] = new_value
            break
    database.write_bank_account(accounts, overwrite=True)

#function for removing account.csv
def remove_account(bank_account_id):
    accounts = database.read_bank_account()

    for account in accounts:
        if account['bank_account_id'] == bank_account_id:
            print("Account confirmed, deleteing...")

    updated_accounts = []
    for account in accounts:
        if account['bank_account_id'] != bank_account_id:
            updated_accounts.append(account)

    if len(updated_accounts) == len(accounts):
        print("No account was found with that ID")
        return
    
    database.write_bank_account(updated_accounts, overwrite=True)