#imports
from services import database
from models import transaction
import uuid 


# Function for reading all recurring expenses
def show_recurring_expenses():
    recurring_expenses = database.read_recurring_expenses()

    if not recurring_expenses:
        print("There are no recurring expenses")
        return

    print("Name | Amount | Category | Frequency | Date Paid | Bank Account")
    print("--------------------------------------")
    for index, expense in enumerate(recurring_expenses):
        print(f"{index + 1}. {expense['name']} | {expense['amount']} | {expense['category']} | {expense['frequency']} | {expense['date']} | {expense['bank_account_id']}")


#function to add recurring expense 
def add_recurring(transaction_dict):
    transaction_dict["id"] = str(uuid.uuid4())

    recurring_object = transaction.recurring_transaction(**transaction_dict)

    recurring_data = {
        "name": recurring_object.name,
        "date": recurring_object.date, 
        "type": recurring_object.type, 
        "category": recurring_object.category,
        "amount": recurring_object.amount, 
        "frequency": recurring_object.frequency, 
        "note": recurring_object.note,
        "bank_account_id": recurring_object.bank_account_id,
        "id": recurring_object.id
    }

    database.write_recurring(recurring_data)

