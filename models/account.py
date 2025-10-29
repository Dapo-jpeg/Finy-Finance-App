class account():
    def __init__(self, bank_account_id, name, currency="NGN", balance="", account_type="", starting_balance="0.0", note=""):
        self.bank_account_id = bank_account_id
        self.name = name
        self.currency = currency
        self.balance = balance
        self.account_type = account_type
        self.starting_balance = starting_balance
        self.note = note

    def __str__(self):
        return f"{self.name}{self.currency}{self.balance}{self.account_type}{self.starting_balance}{self.note}"