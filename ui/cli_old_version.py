
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
def category_menu():
    print("""Which category is it?
1. Foods
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

def user_input_income():
    transactions={}
    transactions["date"] = input("What date is it?(yyyy/mm/dd)\n")
    transactions["type"] = "income"
    while True:
        category_menu()
        try:
            transactions["category"] = int (input("Which category is it?\n"))
            if transactions["category"] <= 0 or transactions["category"] >11:
                print("Please pick a valid number")
                continue
            if transactions["category"] == 1:
                transactions["category"] = "Foods"
                break
            elif transactions["category"] == 2:
                transactions["category"] = "Transportation"
                break
            elif transactions["category"] == 3:
                transactions["category"] = "Communication"
                break
            elif transactions["category"] == 4:
                transactions["category"] = "Housing"
                break
            elif transactions["category"] == 5:
                transactions["category"] = "Personal Care"
                break
            elif transactions["category"] == 6:
                transactions["category"] = "Health and Wellness"
                break
            elif transactions["category"] == 7:
                transactions["category"] = "Education"
                break
            elif transactions["category"] == 8:
                transactions["category"] = "Entertainment"
                break
            elif transactions["category"] == 9:
                transactions["category"] = "Debt payments"
                break
            elif transactions["category"] == 10:
                transactions["category"] = "Pets"
                break
            elif transactions["category"] == 11:
                transactions["category"] = "Others"
                break
        except ValueError:
            print("This value is invalid. Try again please")
    transactions["amount"] = int(input("How much was spent?\n"))
    transactions["note"] = input("Any notes?\n")
    return(transactions)

while True:  
    try: 
        main_menu()
        user_input = int(input("Pick a number please\n"))
        if user_input <=0 or user_input> 10:
            print("Please pick a number between 1 - 10")
            continue
        if user_input == 1:
            user_input_income()
            break
        elif user_input == 2:
            pass
        elif user_input == 3:
            pass
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


