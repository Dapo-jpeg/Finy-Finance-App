#importing csv and path
import csv 
from pathlib import Path

#assigning the csv to a variable
data_file = Path("data/finance_data_v1.csv")

#function to read the csv file 
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
    print(transactions)

#function to write to csv file 
def write_data(transactions):
    
    #Opens csv file to write to
    with open(data_file, 'a',newline='', encoding='utf-8') as data:
        #Giving fieldnames 
        fieldnames = ['date', 'type', 'category', 'amount', 'note', 'id']
        #Assigning data that will go to csv file to writer variable
        writer = csv.DictWriter(data, fieldnames=fieldnames)
        #if the file doesn't exist or file size equals to 0 bytes then set to write_header to True
        write_header = not data_file.exists() or data_file.stat().st_size == 0
        #if write_header is True then go ahead and write header/fieldname but if write_header is False then don't run
        if write_header:
            writer.writeheader()
        #Write the header row based on fieldnames
        writer.writeheader()
        #Write multiple dictionary rows to the csv file
        writer.writerow(transactions)

#function to update value in csv file 
def update_data():
    pass

#function to remove from csv file
def remove_data():
    pass