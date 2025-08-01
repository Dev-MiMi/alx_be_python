

class BankAccount:
    def __init__(self, account_balance, balance=0):
        self.account_balance = account_balance
        self.balance = balance
    def deposit(self, amount):
        return amount + self.account_balance
    def withdraw(self, amount):
        if self.account_balance >= amount:
            return True
        else:
            return False
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")

        


