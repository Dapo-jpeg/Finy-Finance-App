# create a class for the data that we will collect data
class transaction:
    def __init__(self, date, type, category, amount, note, bank_account_id, id):
        # Initiliazing a blueprint that I want to collect these type of data
        self.date = date
        self.type = type # expense or income
        self.category = category
        self.amount = amount
        self.note = note
        self.bank_account_id = bank_account_id
        self.id = id
    
    def __str__(self):
        # if you print an object, it will print everything about that object
        return f"{self.id}{self.date}{self.type}{self.category}{self.amount}{self.note}{self.bank_account_id}"
    
    def display(self):
        # When you print object.display, it will display a neat summary of the transaction
        # I will use this for displaying a neat summary of transactions
        return f"{self.type} - {self.category} - {self.amount}"

# Creating a child class exclusively for expenses
class expense_transaction(transaction):
    def __init__(self, date, type, category, amount, note, bank_account_id, id):
        #Permanently adding the functions of transaction class to expense_transaction class
        super().__init__( date, type, category, amount, note, bank_account_id, id)
        # Change the type to expense 
        self.type = "expense"

#creating a child class exclusively for income
class income_transaction(transaction):
    def __init__(self, date, type, category, amount, note, bank_account_id, id):
        super().__init__(date, type, category, amount, note, bank_account_id, id)
        # Change the type to income
        self.type = "income"

class recurring_transaction(transaction):
    def __init__(self, name, date, type, category, amount, frequency,  note, bank_account_id, id):
        super().__init__(date, type, category, amount, note, bank_account_id, id)
        self.name = name
        self.frequency = frequency