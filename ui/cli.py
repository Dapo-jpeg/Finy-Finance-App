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
    print("4. Remove transaction")
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

def remove_transaction():
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

    #Confirming with user if they want to delete
    user_confirmation = input(f"Are you sure you want to delete ({selected_transaction["date"]} | {selected_transaction["category"]} | {selected_transaction["amount"]} | {transaction['note']})? (yes/no)\n").lower()
    if user_confirmation == "yes":
        #Sending it to transaction_manipulation to delete the selected transaction 
        transaction_manipulation.remove_transaction(selected_transaction['id'])
    elif user_confirmation == "no":
        print("Action cancelled")
    else:
        ValueError
        print("Confirmation not recognized... Action cancelled")


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
    user_input_number = int(input("Pick a number please\n"))

    #Validate user input
    if user_input_number <=0 or user_input_number > 4:
        print("Please pick a number between 1-4")

    #if user picks 1 show all bank account info
    if user_input_number == 1:
        analytics.show_all_account_info()

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
    elif user_input_number == 3:
        pass
    elif user_input_number == 4:
        pass
    elif ValueError:
        print("Please type a number between 1 and 4")





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
                pass
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