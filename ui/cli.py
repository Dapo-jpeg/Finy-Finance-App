#Importing transaction 
from services import transaction_manipulation
from services import account_manipulation
from services import analytics
from services import recurring_manipulation
from datetime import datetime
import schedule

#main menu function to print
def main_menu():
    print("----------Welcome to main menu----------")
    print("1. Add income")
    print("2. Add expense")
    print("3. Change transaction information")
    print("4. Remove transaction")
    print("5. Show bank account balance")
    print("6. Bank account management")
    print("7. Recurring expenses")
    print("8. Show spendings percentage")
    print("9. Show income sources percentage")
    print("10. Monthly Summary")
    print("11. Budgeting")
#! I need to improve and clean up the code on ui. I need to loop through the start 
#!and also loop through each input allowing the user to pick
#function to print the categories so they know what to pick
def income_category_menu():
    print("""Which category is it?
1. Earned income (salary, wages, commision, etc)
2. Investment income (stocks, bonds, crypto, etc)
3. Passive income(digital products, rentals, royalties, etc)
4. Others""")

# function to accept user input for income 
def user_input_income():
    transactions={}
    #Asking for date input
    date_input = input("What date is it?(yyyy/mm/dd)\n")
    date_format = "%Y/%m/%d"
    try:
        #converting date string and date format into actual time
        user_date = datetime.strptime(date_input, date_format)
        #assigning only the date and not the time to the dictonary
        transactions["date"] = datetime.date(user_date)
        print(f"You entered: {user_date.strftime('%Y-%m-%d')}")
    except:
        print("Invalid date format. Please use YYYY/MM/DD")
    
    #Assigining Type income automatically
    transactions["type"] = "income"
    #Making loop to ask for valid input for picking category
    while True:
        #Showing which categories there are
        income_category_menu()
        try:
            user_input_category = int(input("Please pick a number\n"))
            if user_input_category <= 0 or user_input_category >4:
                print("Please pick a valid number")
                continue
            categories = {
                1:"Earned income (salary, wages, commision, etc)",
                2:"Investment income (stocks, bonds, crypto, etc)",
                3:"Passive income(digital products, rentals, royalties, etc)", 
                4:"Others"}
            if user_input_category in categories:
                transactions["category"] = categories[user_input_category]
                break
        except ValueError:
            print("This value is invalid. Try again please!")
    
    while True:
        #showing which bank accounts to pick
        account_list = account_manipulation.print_all_account()
        if not account_list:
            print("No account found. Please create one first")
            break
        try:
            for index, account in enumerate(account_list):
                print(f"{index + 1}. {account['name']} | {account['balance']}")
                continue

            user_input_account = int(input("Which account do you want to use\n"))

            selected_account = account_list[user_input_account - 1]

            transactions["bank_account_id"] = selected_account["bank_account_id"]
            break

        except ValueError:
            print("Invalid input. Try again please.")

    while True:
        try:
            transactions["amount"] = int(input("How much was the transaction?\n"))
            break
        except ValueError:
            print("Please enter a valid number for amount")
    transactions["note"] = input("Any notes?\n")

    return(transactions)

#function to print the categories so they know what to pick
def expense_category_menu():
    print("""Which category is it?
1. Food
2. Transportation
3. Communication
4. Housing
5. Personal Care
6. Health and Wellness
7. Education
8. Entertainment
9. Debt payments
10. Pets 
11. Others""")

#function to accept user input for expense
def user_input_expense():
    transactions={}
    #Asking for date input
    date_input = input("What date is it?(yyyy/mm/dd)\n")
    date_format = "%Y/%m/%d"
    try:
        #converting date string and date format into actual time
        user_date = datetime.strptime(date_input, date_format)
        #assigning only the date and not the time to the dictonary
        transactions["date"] = datetime.date(user_date)
        print(f"You entered: {user_date.strftime('%Y-%m-%d')}")
    except:
        print("Invalid date format. Please use YYYY/MM/DD")
    #Assigning type to expense automatically
    transactions["type"] = "expense"

    #Asking for category and validating it
    while True:
        expense_category_menu()
        try:
            user_input_expense_category = int(input("Which category is it?\n"))
            if user_input_expense_category > 11 or user_input_expense_category <=0:
                print("Please pick a valid number between 1 and 11")
                continue
            categories = {1:"Food", 2:"Transportation", 3:"Communication", 4:"Housing", 5:"Personal Care", 6:"Health and Wellness", 7:"Education", 8:"Entertainment", 9:"Debt payments", 10:"Pets", 11:"Others"}
            if user_input_expense_category in categories:
                transactions["category"] = categories[user_input_expense_category]
                break
        except ValueError:
            print("This value is invalid. Try again please")

    #Picking bank account
    while True:
        #showing which bank accounts to pick
        account_list = account_manipulation.print_all_account()
        if not account_list:
            print("No account found. Please create one first")
            break
        try:
            for index, account in enumerate(account_list):
                print(f"{index + 1}. {account['name']} | {account['balance']}")
                continue

            user_input_account = int(input("Which account do you want to use\n"))

            selected_account = account_list[user_input_account - 1]

            transactions["bank_account_id"] = selected_account["bank_account_id"]
            break

        except ValueError:
            print("Invalid input. Try again please.")

    #Asking for amount input
    transactions["amount"] = int(input("How much was spent?\n"))

    #Asking for note input
    transactions["note"] = input("Any notes?\n")
    #Returning transactions dictionary
    return(transactions)

def change_transaction_info():
    print("Here are all your transactions")
    print("Date | Category | Amount | Note")
    #Read transactions
    transactions_list = transaction_manipulation.print_all_transactions()
    #Display transactions in a numbered list 
    for i, transaction in enumerate(transactions_list):
        print(f"{i+1}. {transaction['date']} | {transaction['category']} | {transaction['amount']} | {transaction['note']}")

    #Ask the user which transaction they want to change
    selected_number = int(input("Enter the number of the transaction you want to change: "))

    #Get the selected transaction based on user input 
    selected_transaction = transactions_list[selected_number - 1]

    #Ask the user which field they want to change and making it lower case
    #*Whenever it is category i should show the different categories for the user to pick
    print("What field do you want to change (date/category/amount/note)")
    field_to_change = input("Field name: ").lower()

    #!Continue the conditional and do it for category and amount 
    if field_to_change == "date":
        #Asking for date input
        date_input = input("What date do you want to change to?(yyyy/mm/dd)\n")
        date_format = "%Y/%m/%d"
        try:
            #converting date string and date format into actual time
            user_date = datetime.strptime(date_input, date_format)
            #assigning only the date and not the time to the dictonary
            new_value = datetime.date(user_date)
            print(f"You entered: {user_date.strftime('%Y-%m-%d')}")
        except:
            print("Invalid date format. Please use YYYY/MM/DD")
    else:
        #Ask what the new value they want to change it to 
        new_value = input("Enter new value: ")

    #Sending all the collected informatino for transaction_manipulation to handle. 
    transaction_manipulation.update_transaction(selected_transaction['id'], field_to_change, new_value)

    #Updating the bank account balance
    analytics.calculate_account_balance(selected_transaction['bank_account_id'])

def remove_transaction():
    print("Here are all your transactions")
    print("Date | Category | Amount | Note")

    #Read transactions
    transactions_list = transaction_manipulation.print_all_transactions()
    #Display transactions in a numbered list 
    for i, transaction in enumerate(transactions_list):
        print(f"{i+1}. {transaction['date']} | {transaction['category']} | {transaction['amount']} | {transaction['note']}")

    #Ask the user which transaction they want to change
    selected_number = int(input("Enter the number of the transaction you want to remove: "))

    #Get the selected transaction based on user input 
    selected_transaction = transactions_list[selected_number - 1]

    #Confirming with user if they want to delete
    user_confirmation = input(f"Are you sure you want to delete ({selected_transaction["date"]} | {selected_transaction["category"]} | {selected_transaction["amount"]} | {selected_transaction['note']})? (yes/no)\n").lower()
    if user_confirmation == "yes":
        #Sending it to transaction_manipulation to delete the selected transaction 
        transaction_manipulation.remove_transaction(selected_transaction['id'])
    elif user_confirmation == "no":
        print("Action cancelled")
    else:
        ValueError
        print("Confirmation not recognized... Action cancelled")

    #Updating the bank account balance
    analytics.calculate_account_balance(selected_transaction['bank_account_id'])



#function to show bank account balance only 
def bank_account_balance():
    analytics.show_bank_balance()

#function for bank account category for number 6
def bank_account_CRUD_menu():
    print("Please pick an option")
    print("1. Show bank account information")
    print("2. Add new bank account")
    print("3. Update bank account info")
    print("4. Remove bank account")

#function for bank account manipulation for number 6
def bank_account_manipulation():
    bank_account_CRUD_menu()

    #Ask user for input
    try:
        user_input_number = int(input("Pick a number please\n"))
    except ValueError:
        print("Please pick a number between 1-4")

    #Validate user input
    if user_input_number <=0 or user_input_number > 4:
        print("Please pick a number between 1-4")

    #if user picks 1 show all bank account info
    if user_input_number == 1:
        accounts = account_manipulation.print_all_account()
        print("ID | Account name | Currency | Balance")
        print("--------------------------------------")
        for index, account in enumerate(accounts):
            print(f"{index +1}. {account['name']} | {account['currency']} | {account['balance']}")

    #if user picks 2 call add bank account function in account manipulation 
    elif user_input_number == 2:
        account_input={}

        account_input['name'] = input("What is the name of the bank account?\n")

        currency_input = input("Currency is set to NGN. Do you want to change it?(yes/no)\n").lower()
        if currency_input == "yes":
            account_input["currency"] = input("Which currency (Use 3 letter abbreviation)")
        elif currency_input == "no":
            account_input['currency'] = "NGN"
        elif ValueError:
            print("Invalid input. Please type yes or no")
        
        account_input['balance'] = ''
        account_input['account_type'] = input("What is the account type? (Examples = Checking, Savings, Joint account, etc)\n").lower()

        account_input['starting_balance'] = int(input("What is the starting balance for this account?\n"))

        note_input = input("Any account note? (yes/no)\n").lower()
        if note_input == "yes":
            account_input['note'] = input("Please type your note\n")
        elif note_input == "no":
            account_input['note'] = ''
        elif ValueError:
            print("Invalid input. Please type yes or no")

        account_manipulation.add_bank_account(account_input)
        print("Account added successfully")
    
    #if user picks 3, allow them to update it. 
    elif user_input_number == 3:
        print("Here are your all bank account information")
        print("Account name | Currency | Account type | Starting balance | Note")

        account_list = account_manipulation.print_all_account()
        
        for index, account in enumerate(account_list):
            print(f"{index + 1}. {account['name']} | {account['currency']} | {account['account_type']} | {account['starting_balance']} | {account['note']}")

        selected_number = int(input("Enter the number of the account details you want to change: "))

        selected_account = account_list[selected_number - 1]

        while True:
            try: 
                print("What field do you want to change")
                print("1. Account name")
                print("2. Currency")
                print("3. Account Type")
                print("4. Starting balance")
                print("5. Note")

                fields = {
                    1:"name",
                    2:"currency",
                    3:"account_type",
                    4:"starting_balance",
                    5:"note"
                    }
                user_change_field = int(input("Number: "))
                if user_change_field in fields:
                    field_to_change = fields[user_change_field]
                    break
            except ValueError:
                print("This value is invalid. Try again please")


        new_value = input("Enter new value: ")

        account_manipulation.update_account(selected_account['bank_account_id'], field_to_change, new_value)

        print("Account details successfully updated")

        #Update the bank account balance
        analytics.calculate_account_balance(selected_account["bank_account_id"])
    
    elif user_input_number == 4:
        print("Here are all your accounts")
        print("Account name | Currency | Account type | Starting balance | Note")

        account_list = account_manipulation.print_all_account()

        for index, account in enumerate(account_list):
            print(f"{index + 1}. {account['name']} | {account['currency']} | {account['account_type']} | {account['starting_balance']} | {account['note']}")

        selected_number = int(input("Enter the number of the account you want to delete\n"))

        selected_account = account_list[selected_number - 1]

        user_confirmation = input(f"Are you sure you want to delete ({selected_account['name']} | {selected_account['currency']} | {selected_account['account_type']} | {selected_account['starting_balance']} | {selected_account['note']})? (yes/no)\n").lower()
        if user_confirmation == "yes":
            account_manipulation.remove_account(selected_account['bank_account_id'])
        elif user_confirmation == "no":
            print("Action cancelled")
        else:
            ValueError
            print("Confirmation not recognized... Action cancelled")

        print("Account successfully deleted")

        #Update the bank account balance
        analytics.calculate_account_balance(selected_account["bank_account_id"])

    elif ValueError:
        print("Please type a number between 1 and 4")


def recurring_expenses():
    print("Please pick an option")
    print("1. Show all recurring expenses")
    print("2. Add a recurring expense")
    print("3. Update a recurring expense")
    print("4. Delete a recurring expense")

    try:
        user_input_recurring = int(input("Please pick a number between 1-4\n"))
    except ValueError:
        print("Please type a number between 1-4")

    if user_input_recurring <=0 or user_input_recurring > 4:
        print("Please type a number between 1-4")
    #-------------------------------------------------------
    if user_input_recurring == 1:
        recurring_manipulation.show_recurring_expenses()
    #----------------------------------------------------------
    if user_input_recurring == 2:
        #calling expense function
        transaction_dict = user_input_expense()
        #duplicating dictionary and removing frequency part
        expense_dict = transaction_dict.copy()

        # Ask for a name for the subscription
        transaction_dict["name"] = input("What do you want to name this recurring transaction? \n")
        # Asking for frequency
        while True:
            transaction_dict["frequency"] = input("How frequent (daily, weekly, monthly, yearly)\n").lower()
            options = ["daily", "weekly", "monthly", "yearly"]
            if transaction_dict["frequency"] not in options:
                print("Please type a valid input (daily, weekly, monthly, yearly) \n")
            else: 
                break
        
        print("Recurring expenses added successfully")
        #sending different dictionaries to write to different csv
        transaction_manipulation.add_expense(expense_dict)
        recurring_manipulation.add_recurring(transaction_dict)
        analytics.calculate_account_balance(transaction_dict['bank_account_id'])
    #---------------------------------------------------------
    #update a recurring expense
    if user_input_recurring == 3:
        print("Here are all the recurring expenses")
        recurring_list = recurring_manipulation.show_recurring_expenses()

        #Ask the user which recurring expense they want to change
        selected_number = int(input("Enter the number of the recurring expense you want to change: "))

        selected_recurring = recurring_list[selected_number - 1]

        print("What field do you want to change (name, date, amount, frequency, category, note)")
        field_to_change = input("Field name: ").lower()

        #!Continue the conditional and do it for category and amount 
        if field_to_change == "date":
            #Asking for date input
            date_input = input("What date do you want to change to?(yyyy/mm/dd)\n")
            date_format = "%Y/%m/%d"
            try:
                #converting date string and date format into actual time
                user_date = datetime.strptime(date_input, date_format)
                #assigning only the date and not the time to the dictonary
                new_value = datetime.date(user_date)
                print(f"You entered: {user_date.strftime('%Y-%m-%d')}")
            except:
                print("Invalid date format. Please use YYYY/MM/DD")
        else:
            #Ask what the new value they want to change it to 
            new_value = input("Enter new value: ")

        #sending all info to recurring_manipulation to handle
        recurring_manipulation.update_recurring_expenses(selected_recurring["id"], field_to_change, new_value)

        print("Successfully updated expenses")

        #update the bank account balance
        analytics.calculate_account_balance(selected_recurring['bank_account_id'])
    #------------------------------------------------------------------------------------------------------------
    if user_input_recurring == 4:
        print("Here are all the recurring expenses")
        recurring_list = recurring_manipulation.show_recurring_expenses()

        #Ask the user which recurring expense they want to change
        selected_number = int(input("Enter the number of the recurring expense you want to change: "))

        selected_recurring = recurring_list[selected_number - 1]

        user_confirmation = input(f"Are you sure you want to delete ({selected_recurring["name"]} | {selected_recurring["date"]} | {selected_recurring["category"]} | {selected_recurring["frequency"]} | {selected_recurring["amount"]} | {selected_recurring['note']})? (yes/no) \n").lower()

        if user_confirmation == "yes":
            # Send data to recurring manipulation
            recurring_manipulation.remove_recurring_expense(selected_recurring["id"])
            print("Successfully removed expense")
        elif user_confirmation == "no":
            print("Action cancelled")
        else :
            ValueError
            print ("Confirmation not recognized... Action cancelled")
schedule.every()
#! I have to make another function that constantly checks the date so it can call up the recurring expense again (I will do this after switching my database to SQL)

def start():
    while True: 
        try: 
            schedule.run_pending()
            main_menu()
            user_input = int(input("Pick a number please\n"))

            if user_input <=0 or user_input> 11:
                print("Please pick a number between 1 - 10")
                continue
            
            if user_input == 1:
                #Transaction dict = to the transaction that was returned in user_input_income function
                transactions_dict = user_input_income()
                #sent as argument to transaction_manipulation
                transaction_manipulation.add_income(transactions_dict)
                print("Added transaction successfully")
                #Recalculate balance for only that account and rewrites 
                analytics.calculate_account_balance(transactions_dict['bank_account_id'])
                break
            elif user_input == 2:
                #Transaction dict = to the transaction that was returned in user_input_expense function
                transactions_dict = user_input_expense()
                #sent as argument to transaction_manipulation
                transaction_manipulation.add_expense(transactions_dict)
                print("Added transaction successfully")
                #Recalculate balance for only that account and rewrites 
                analytics.calculate_account_balance(transactions_dict['bank_account_id'])
                break
            elif user_input == 3:
                change_transaction_info()
                print("Updated Transaction successfully")
                break
            elif user_input == 4:
                remove_transaction()
                print("Transaction removed successfully")
                break
            elif user_input == 5:
                bank_account_balance()
                break
            elif user_input == 6:
                bank_account_manipulation()
                break
            elif user_input == 7:
                recurring_expenses()
                break
            elif user_input == 8:
                pass
            elif user_input == 9:
                pass
            elif user_input == 10:
                pass
            elif user_input == 11:
                pass
        #if they type anything else then print invalid input
        except ValueError:
            print("Invalid input. Please try again")