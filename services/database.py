#importing csv and path 
import csv 
from pathlib import Path

#assigning the csv to a variable
data_file = Path("data/finance_data_v1.csv")

#function to read the csv file 
def read_data():
    
    #Making a dict called transactions
    transactions = [
        {
        "id":1,
        "date":"2025-10-15",
        "type":"expense",
        "category":"Food",
        "amount":5000,
        "note":"Lunch"
        },
        {
        "id":2,
        "date":"2025-10-16",
        "type":"expense",
        "category":"Food",
        "amount":10000,
        "note":"Dinner"
        }
    ]
    
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
    
    #Skips the first line which is the field name
    #next(reader)

#function to write to csv file 
def write_data(transactions):
    
    #Opens csv file to write to
    with open(data_file, 'w',newline='', encoding='utf-8') as data:
        #Giving fieldnames 
        fieldnames = ['id', 'date', 'type', 'category', 'amount', 'note']
        #Assigning data that will go to csv file to writer variable
        writer = csv.DictWriter(data, fieldnames=fieldnames)
        #Write the header row based on fieldnames
        writer.writeheader()
        #Write multiple dictionary rows to the csv file
        writer.writerows(transactions)

#function to update value in csv file 
def update_data():
    pass

#function to remove from csv file
def remove_data():
    pass