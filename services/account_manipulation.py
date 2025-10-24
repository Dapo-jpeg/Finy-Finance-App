import csv
from pathlib import Path

account_data_file = Path("data/account.csv")
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


# function for adding an account to csv
def add_bank_account():
    pass
    #read and write to account.csv

#function for updating account.csv


#function for removing account.csv