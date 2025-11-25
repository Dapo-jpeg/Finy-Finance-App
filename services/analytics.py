from services import database

#calculate bank balance 
def calculate_account_balance(bank_account_id):
    #read all accounts and transactions
    transactions = database.fetch_many_transactions()
    accounts = database.fetch_many_bank_accounts()

    #say there are no account if no accounts found
    if not accounts or len(accounts) == 0 :
        print("There are no bank accounts")
        return

    #say there are no transactions found
    if not transactions or len(transactions) == 0 :
        print("There are no transactions with this bank account.")
        return

    #filter to get transactions with bank_account_id
    filtered_transactions = []
    for transaction in transactions:
        if transaction['bank_account_id'] == bank_account_id:
            filtered_transactions.append(transaction)

    #Get starting balance from account
    starting_balance = 0
    for account in accounts:
        if bank_account_id == account['bank_account_id']:
            starting_balance = float(account['starting_balance'])
            break

    #sum of all expense transactions and sum of all income transactions
    expense_sum = 0
    income_sum = 0
    for transaction in filtered_transactions:
        amount = float(transaction["amount"])
        if transaction["type"] == "expense":
            expense_sum += amount
        elif transaction["type"] == "income":
            income_sum += amount

    #balance = income sum - expense sum + starting balance
    net_balance = starting_balance + (income_sum - expense_sum)

    database.update_bank_balance(bank_account_id, net_balance)

#function to calculate all the bank account balances
def update_all_account_balance():
    #Read all accounts
    all_accounts = database.fetch_many_bank_accounts()

    #check if there are any accounts 
    if not all_accounts or len(all_accounts) == 0:
        print("There are no bank accounts")
        return

    #iterate and calculate the balance of each bank account
    for each_account in all_accounts:
        bank_account_id = each_account["bank_account_id"]
        new_balance = calculate_account_balance(bank_account_id)


#function showing bank account balance
def show_bank_balance():
    #calculate all bank accounts balances
    update_all_account_balance()
    
    #read all accounts and store them in accounts
    accounts = database.fetch_many_bank_accounts()

    #if account empty tell user there are no accounts
    if not accounts:
        print("No accounts found. Please create one")
        return
    
    #Showing the accounts & balnces to user 
    print("ID | Account name | Currency | Balance")
    print("--------------------------------------")
    for index, account in enumerate(accounts):
        print(f"{index + 1}. {account['name']} | {account['currency']} | {account['balance']}")

def show_all_account_info():
    #calculate all bank accounts balances
    update_all_account_balance()
    
    #read all accounts and store them in accounts
    accounts = database.fetch_many_bank_accounts()

    #if account empty tell user there are no accounts
    if not accounts:
        print("No accounts found. Please create one")
        return
    
    #Showing the accounts & balnces to user 
    print("ID | Account name | Currency | Balance | Account Type | Starting Balance | Note")
    print("--------------------------------------")
    for index, account in enumerate(accounts):
        print(f"{index + 1}. {account['name']} | {account['currency']} | {account['balance']} | {account['account_type']} | {account['starting_balance']} | {account['note']}")



#function showing categorical incomes

#function showing categorical expenses

#function showing monthly summary 
    #shows income amount last month
    #shows expenses amount last month
    #shows profit and loss
    #cash flow
    #financial ratios