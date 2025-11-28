#imports
from services import database
from models import transaction
import uuid 
import datetime
import schedule


def automate_recurring_expense():
    today_date = datetime.date.today()
    all_recurring_expenses = database.fetch_many_recurring_expenses()
    #look for all recurring expenses that have next pay date for today and have not already been paid for then adds them to transaction list
    for recurring_expense in all_recurring_expenses:
        if (recurring_expense["next_pay_date"] == today_date and recurring_expense["last_date_paid"]!= today_date) or recurring_expense["next_pay_date"] == None:
            expense = {}
            expense["id"] = str(uuid.uuid4())
            expense["date"] = str(today_date)
            expense["type"] = recurring_expense["type"]
            expense["category"] = recurring_expense ["category"]
            expense["amount"] = recurring_expense["amount"]
            expense["note"] = recurring_expense["name"] #Just so when they go through transaction list they know what they money is goes
            expense["bank_account_id"] = recurring_expense["bank_account_id"]

            #Sending necessary info for expense
            database.insert_transaction(expense)

            expense["id"] = recurring_expense["id"]
            expense["name"] = recurring_expense["name"]
            expense["frequency"] = recurring_expense["frequency"]
            expense["last_date_paid"] = str(today_date)
            expense["note"] = recurring_expense["note"]
            del expense["date"]
            print(f"shoudl have worked {expense}")

            #update last date paid
            if recurring_expense["frequency"] == "daily":
                interval_date = datetime.timedelta(days = 1)
                expense["next_pay_date"] = today_date + interval_date
                database.update_recurring_expense(expense)

            elif recurring_expense["frequency"] == "weekly":
                interval_date = datetime.timedelta(weeks = 1)
                expense["next_pay_date"] = today_date + interval_date
                database.update_recurring_expense(expense)

            elif recurring_expense["frequency"] == "monthly":
                # Adding exactly one month and if the month goes more than 12(dec) reset the month to 1(jan) and add one to the year 
                month = today_date.month + 1
                year = today_date.year
                if month > 12:
                    month = 1
                    year += 1
                interval_date = today_date.replace(year=year, month=month)
                expense["next_pay_date"] = str(interval_date)
                database.update_recurring_expense(expense)
            
            elif recurring_expense["frequency"] == "yearly":
                year = today_date.year + 1
                interval_date = today_date.replace(year=year)
                expense["next_pay_date"] = str(interval_date)
                database.update_recurring_expense(expense)







