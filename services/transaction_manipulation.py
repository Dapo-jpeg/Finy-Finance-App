#importing files
from services import database
from models import transaction
import uuid

#function to add income 
def add_income(transactions_dict):
    #TODO: 1. Generate unique id using uuid
    transactions_dict["id"] = str(uuid.uuid4())
    #TODO: 2. Validate and create object
    # Validating object
    #* Will do later
    # Creating an object 
    income_object = transaction.income_transaction(**transactions_dict)
    #Converting object to dict before sending
    transaction_data = {
        "date": income_object.date, 
        "type": income_object.type, 
        "category": income_object.category,
        "amount": income_object.amount, 
        "note": income_object.note, 
        "id": income_object.id
    }
    #TODO: 3. Pass data to database.py
    database.write_data(transaction_data)
#function to add expense
def add_expense(transaction_dict):
    #TODO: Generate unique uuid 
    transaction_dict["id"] = str(uuid.uuid4())
    #TODO: Validate and create object
    # validating data
    #* will do later
    # Creating object
    expense_object = transaction.expense_transaction(**transaction_dict)
    # Converting object to dict before sending
    transaction_data = {
        "date": expense_object.date, 
        "type": expense_object.type, 
        "category": expense_object.category, 
        "amount": expense_object.amount, 
        "note": expense_object.note, 
        "id": expense_object.id
    }
    #TODO: Pass data to database.py for writing
    database.write_data(transaction_data)
    pass

#function to update income 


#function to update expense 


#function to remove income 

#function to remove expense