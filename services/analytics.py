from services import database

#function showing bank account balance
def show_bank_balance():
    #read all accounts and store them in accounts
    accounts = database.read_bank_account()

    #if account empty tell user there are no accounts
    if not accounts:
        print("No accounts found. Please create one")
        return
    
    #Showing the accounts & balnces to user 
    print("ID | Account name | Currency | Balance")
    print("--------------------------------------")
    for index, account in enumerate(accounts):
        print(f"{index + 1}. {account['name']} | {account['currency']} | {account['balance']}")


#function showing categorical incomes

#function showing categorical expenses

#function showing monthly summary 
    #shows income amount last month
    #shows expenses amount last month
    #shows profit and loss
    #cash flow
    #financial ratios