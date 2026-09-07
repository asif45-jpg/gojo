class Bank:
    def __init__(self, Name, balance=0):
        self.Name = Name
        self.balance = balance
    def deposit(self,amount):
        self.amount = amount
        if amount < 0 :
            print("Amount must be positive")
        else:
            self.balance = amount+balance
        