class account():
    def __init__(self, bank_account_id, name, currency="NGN", starting_balance="0.0", account_type="", note=""):
        self.bank_account_id = bank_account_id
        self.name = name
        self.currency = currency
        self.starting_balance = starting_balance
        self.account_type = account_type
        self.note = note

    def __str__(self):
        return f"{self.name}{self.currency}{self.starting_balance}{self.account_type}{self.note}"