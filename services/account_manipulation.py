from services import database
from models import account
import uuid

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


#function for removing account.csv