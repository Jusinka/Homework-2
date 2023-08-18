import uuid
from decimal import Decimal
import datetime


class BankAccount:
    def __init__(self, account_name, initial_balance=0):
        self.account_name = account_name
        self.account_id = uuid.uuid4()
        self.balance = Decimal(initial_balance)
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += Decimal(amount)
            self.transactions.append((Decimal(amount), 'deposit', datetime.datetime.now()))

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= Decimal(amount)
            self.transactions.append((Decimal(amount), 'withdrawal', datetime.datetime.now()))

    def get_balance(self):
        return self.balance

    def apply_commission(self):
        commission = self.balance * Decimal('0.01')
        self.balance -= commission
        self.transactions.append((commission, 'commission', datetime.datetime.now()))

    def print_transactions(self):
        for transaction in self.transactions:
            amount, transaction_type, transaction_date = transaction
            print(f"{transaction_date}: {transaction_type} - {amount}")


# Приклад використання
if __name__ == "__main__":
    account = BankAccount("John's Account", 1000)

    account.deposit(500)
    account.withdraw(200)
    account.apply_commission()

    print("Current balance:", account.get_balance())
    account.print_transactions()