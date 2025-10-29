#Importing transaction 
from services import transaction_manipulation

#main menu function to print
def main_menu():
    print("----------Welcome to main menu----------")
    print("1. Add income")
    print("2. Add expense")
    print("3. Change transaction information")
    print("4. Remove income/expense")
    print("5. Show account balance")
    print("6. Show spendings percentage")
    print("7. Show income sources percentage")
    print("8. Recurring expenses")
    print("9. Monthly Summary")
    print("10. Budgeting")

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


def start():
    while True:  
        try: 
            main_menu()
            user_input = int(input("Pick a number please\n"))
            if user_input <=0 or user_input> 10:
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
        #This code is not working
        except ValueError:
            print("Invalid input. Please try again")