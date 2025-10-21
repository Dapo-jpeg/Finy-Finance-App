# create a class for the data that we will collect data
class transaction:
    def __init__(self, id, date, type, category, amount, note):
        # Initiliazing a blueprint that I want to collect these type of data
        self.id = id
        self.date = date
        self.type = type # expense or income
        self.category = category
        self.amount = amount
        self.note = note
    
    def __str__(self):
        # if you print an object, it will print everything about that object
        return f"{self.id}{self.date}{self.type}{self.category}{self.amount}{self.note}"
    
    def display(self):
        # When you print object.display, it will display a neat summary of the transaction
        # I will use this for displaying a neat summary of transactions
        return f"{self.category} - {self.amount}"

# Creating a child class exclusively for expenses
class expense_transaction(transaction):
    def __init__(self, date, type, category, amount, note, id):
        super().__init__(id, date, type, category, amount, note)
        # Change the type to expense 
        self.type = "Expense"

#creating a child class exclusively for income
class income_transaction(transaction):
    def __init__(self, date, type, category, amount, note, id):
        super().__init__(id, date, type, category, amount, note)
        # Change the type to income
        self.type = "Income"