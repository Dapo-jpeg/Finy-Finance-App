#importing csv and path
import csv 
from pathlib import Path

#assigning the csv to a variable
data_file = Path("data/finance_data_v1.csv")
account_data_file = Path("data/account.csv")
recurring_expenses_data = Path("data/recurring_expenses.csv")

#function to read the transaction csv file 
def read_data():
    
    #Making a list of dict called transactions
    transactions = []
    #if there is no data in the csv file then say no transactions made
    if not data_file.exists():
        print("No transactions have been made")
        return transactions
    
    # Opens csv file and reads the values and assigns them to reader
    with open(data_file,'r', newline='', encoding='utf-8') as data:
        reader = csv.DictReader(data)
        
        #Iterate and read out each line in the csv file
        for row in reader:
            transactions.append(row)
    return(transactions)

#function to write to transaction csv file 
def write_data(transactions, overwrite=False):
    
    #Giving fieldnames 
    fieldnames = ['date', 'type', 'category', 'amount', 'note', 'bank_account_id', 'id']
    mode = 'w' if overwrite else 'a'
    
    #Opens csv file to write to
    with open(data_file, mode ,newline='', encoding='utf-8') as data:
        #Assigning data that will go to csv file to writer variable
        writer = csv.DictWriter(data, fieldnames=fieldnames)
        
        #if the file doesn't exist or file size equals to 0 bytes then set to write_header to True
        write_header = not data_file.exists() or data_file.stat().st_size == 0
        #if write_header is True then go ahead and write header/fieldname but if write_header is False then don't run
        if write_header or overwrite:
            writer.writeheader()
        
        #If overwrite= True then completely overwrite file else just append row
        if overwrite:
            #Write multiple rows
            writer.writerows(transactions)
        else:       
            #Write append dictionary row to the csv file
            writer.writerow(transactions)


#function to read account.csv
def read_bank_account():
    #making a list of dict called accounts
    accounts = []
    #if there is no data found then print no accounts currently
    if not account_data_file.exists():
        print("No bank accounts currently")
        return accounts
    #Open csv to read
    with open(account_data_file, 'r', newline='', encoding= 'utf-8') as data:
        # assign the all files that are being read to reader
        reader = csv.DictReader(data)
        
        #iterate reading each line 
        for row in reader:
            accounts.append(row)
    return(accounts)

def write_bank_account(account_input_data, overwrite=False):
    #Giving fieldnames
    fieldnames = ['name', 'currency', 'balance', 'account_type', 'starting_balance', 'note', 'bank_account_id']
    mode = 'w' if overwrite else 'a'

    #open csv file to write to 
    with open(account_data_file, mode, newline='', encoding='utf-8') as account_data:
        writer = csv.DictWriter(account_data, fieldnames=fieldnames)

        #Not repeat writing header fields
        write_header = not account_data_file.exists() or account_data_file.stat().st_size == 0
        if write_header or overwrite:
            writer.writeheader()

        #Write to append dictionary row to the csv file
        if overwrite:
            writer.writerows(account_input_data)
        else:
            writer.writerow(account_input_data)


#function to read recurring_expenses.csv
def read_recurring_expenses():
    recurring_expenses = []

    if not recurring_expenses_data.exists():
        print("There are no recurring expenses")
        return recurring_expenses
    
    with open(recurring_expenses_data, 'r', newline= '', encoding='utf-8') as recurring_expenses_file:
        reader = csv.DictReader(recurring_expenses_file)

        for row in reader:
            recurring_expenses.append(row)
    return (recurring_expenses)

def write_recurring(recurring_data, overwrite=False):

    mode = "w" if overwrite else "a"

    fieldnames = ['name', 'date', 'type', 'category', 'amount', 'frequency', 'note', 'bank_account_id', 'id']

    with open(recurring_expenses_data, mode, newline="", encoding="utf-8") as recurring_expenses_file:
        writer = csv.DictWriter(recurring_expenses_file, fieldnames=fieldnames)

        write_header =  not recurring_expenses_data.exists() or recurring_expenses_data.stat().st_size == 0

        if write_header or overwrite :
            writer.writeheader()

        if overwrite:
            writer.writerows(recurring_data)
        else:
            writer.writerow(recurring_data)
            
