#Importing transaction 
from services import transaction_manipulation
from services import account_manipulation
from services import analytics

#main menu function to print
def main_menu():
    print("----------Welcome to main menu----------")
    print("1. Add income")
    print("2. Add expense")
    print("3. Change transaction information")
    print("4. Remove income/expense")
    print("5. Show bank account balance")
    print("6. Bank account management")
    print("7. Show spendings percentage")
    print("8. Show income sources percentage")
    print("9. Recurring expenses")
    print("10. Monthly Summary")
    print("11. Budgeting")

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
    transactions["date"] = input("What date is it?(yyyy/mm/dd)\n")
    #Assigining Type income automatically
    transactions["type"] = "income"
    #Making loop to ask for valid input for picking category
    while True:
        #Showing which categories there are
        income_category_menu()
        try:
            user_input_category = int(input("Which Category is it\n"))
            if user_input_category <= 0 or user_input_category >4:
                print("Please pick a valid number")
                continue
            categories = {1:"Earned income (salary, wages, commision, etc)", 2:"Investment income (stocks, bonds, crypto, etc)", 3:"Passive income(digital products, rentals, royalties, etc)", 4:"Others"}
            if user_input_category in categories:
                transactions["category"] = categories[user_input_category]
                break
        except ValueError:
            print("This value is invalid. Try again please")
    transactions["amount"] = int(input("How much was the transaction?\n"))
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
    transactions["date"] = input("What date is it?(yyyy/mm/dd)\n")
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
    #Asking for amount input
    transactions["amount"] = int(input("How much was spent?\n"))
    #Asking for note input
    transactions["note"] = input("Any notes?\n")
    #Returning transactions dictionary
    return(transactions)

#function to show bank account balance only 
def bank_account_balance():
    pass 

#function to show the different bank accounts from account.csv for the user to pick
def bank_account_topick():
    pass
    # calls read_bank_account function from account_manipulation.py
    # prints out all accounts 
    #//Working on this now
    account_manipulation.read_bank_account()
    # assign to dict
    account_dict_topick = {
        "bank_account_id" : account_manipulation.read_bank_account}
    # create a variable called picked option

    # ask user for input 
    # match user input to the dict then update emapty variable called picked option with user input

#function for bank account category for number 6
def bank_account_menu():
    print("Please pick an option")
    print("1. Show bank account information")
    print("2. Add new bank account")
    print("3. Update bank account info")
    print("4. Remove bank account")

#function for bank account manipulation for number 6
def bank_account_manipulation():
    bank_account_menu()
    user_input = int(input("Pick a number please"))
    if user_input <=0 or user_input > 4:
        print("Please pick a number between 1-4")
    #if user picks 1 
    if user_input == 1:
        #call function add_bank_account from account_manipulation.py
        #TODO: working on this now
        account_manipulation.add_bank_account
    #elif user picks 2
    elif user_input == 2:
        #call function to ask which bank account 
        bank_account_topick()
        user_input_2 = int(input("Pick a number please"))
        #if user picks (number)
        if user_input_2 == 1:
            #call show_account_info from analytics.py
            pass
    #elif user picks 3
        #call function to ask which bank account
            #if user picks (number)
                #call show_account_info from analytics.py
                    #ask user which part they want to update
                        #if user picks (number)
                        #call function from account_manipulation.py to allow changing that part
    # elif user picks 4
        #call function to ask which bank account
            #if user picks(number)
                #call remove_bank_account from account_manipulation.py
    pass

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
    print("What field do you want to change (date/category/amount/note)")
    field_to_change = input("Field name: ").lower()

    #Ask what the new value they want to change it to 
    new_value = input("Enter new value: ")

    #Sending all the collected informatino for transaction_manipulation to handle. 
    transaction_manipulation.update_transaction(selected_transaction['id'], field_to_change, new_value)


def start():
    while True:  
        try: 
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
                break
            elif user_input == 2:
                #Transaction dict = to the transaction that was returned in user_input_expense function
                transactions_dict = user_input_expense()
                #sent as argument to transaction_manipulation
                transaction_manipulation.add_expense(transactions_dict)
                print("Added transaction successfully")
                break
            elif user_input == 3:
                change_transaction_info()
                print("Updated Transaction successfully")
                break
            elif user_input == 4:
                pass
            elif user_input == 5:
                pass
            elif user_input == 6:
                pass
            elif user_input == 7:
                pass
            elif user_input == 8:
                pass
            elif user_input == 9:
                pass
            elif user_input == 10:
                pass
            elif user_input == 11:
                pass
        #This code is not working
        except ValueError:
            print("Invalid input. Please try again")