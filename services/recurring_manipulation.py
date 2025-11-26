#imports
from services import database
from models import transaction
import uuid 
import datetime
import schedule


# Function for reading all recurring expenses
def show_recurring_expenses():
    recurring_expenses = database.fetch_many_recurring_expenses()

    if not recurring_expenses:
        print("There are no recurring expenses")
        return

    print("Name | Amount | Category | Frequency | Bank Account | Date paid ")
    print("--------------------------------------")
    for index, expense in enumerate(recurring_expenses):
        print(f"{index + 1}. {expense['name']} | {expense['amount']} | {expense['category']} | {expense['frequency']} | {expense['date']}")
    #! I need to fix the expense['bank_account_id'] above by joining the tables using SQL
    return recurring_expenses


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

    database.insert_recurring_expense(recurring_data)

def update_recurring_expenses(expense_id, field_to_change, new_value):
    all_recurring_expenses = database.fetch_many_recurring_expenses()

    if not all_recurring_expenses:
        print("There are no recurring expenses")
        return

    for expense in all_recurring_expenses:
        if expense["id"] == expense_id:
            print("Transaction found, updating...")
        
            #validating field_to_change and new_value
            if field_to_change not in ["name", "date", "amount", "frequency", "category", "note"]:
                print("Invalid field name")
                return
            
            if field_to_change == "amount":
                if int(new_value) <= 0:
                    print("Invalid value. Amount must be greater than 0")
                    return
            
            #update expense
            expense[field_to_change] = new_value
            database.update_recurring_expense(expense)
            break

def remove_recurring_expense(expense_id):
    all_recurring_expenses = database.fetch_many_recurring_expenses()

    if not all_recurring_expenses:
        print("There are no recurring expenses")
        return

    for expense in all_recurring_expenses:
        if expense["id"] == expense_id:
            print("Transaction found, updating...")
    
    # sending it to be rewritten
    database.delete_recurring_expense(expense_id)

def automate_recurring_expense():
    recurring_expenses = database.fetch_many_recurring_expenses()

    today_date = datetime.date.today()
    for recurring_expense in recurring_expenses:
        expense = {}
        expense["date"] = today_date
        expense["type"] = recurring_expense["type"]
        expense["category"] = recurring_expense ["type"]
        expense["amount"] = recurring_expense["amount"]
        expense["note"] = recurring_expense["note"]
        expense["bank_account_id"] = recurring_expense["bank_account_id"]
        if recurring_expense["frequency"] == "daily":
            schedule.every().day.do (database.insert_many_transactions(expense))

        elif recurring_expense["frequency"] == "weekly":
            schedule.every().week.do (database.insert_many_transactions(expense))

        elif recurring_expense["frequency"] == "monthly":
            schedule.every().month.do (database.insert_many_transactions(expense))
        
        elif recurring_expense["frequency"] == "yearly":
            schedule.every().year (database.insert_many_transactions(expense))

        if recurring_expense["date"] == today_date: #! Wont work the same month and day but not same year or vice versa
            expense = {}
            expense["date"] = today_date
            expense["type"] = recurring_expense["type"]
            expense["category"] = recurring_expense ["type"]
            expense["amount"] = recurring_expense["amount"]
            expense["note"] = recurring_expense["note"]
            expense["bank_account_id"] = recurring_expense["bank_account_id"]
            database.insert_many_transactions(expense)


    pass