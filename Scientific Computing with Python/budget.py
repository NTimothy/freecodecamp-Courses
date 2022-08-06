class Category:
    def __init__(self, category_name="Misc"):
        self.ledger = []
        self.balance = 0
        self.name = str(category_name.lower().capitalize())

    def __repr__(self):
        return self.name

    def deposit(self, amount, description=""):
        transaction = {}
        transaction["amount"] = (amount)
        transaction["description"] = description
        self.ledger.append(transaction)
        self.balance += amount
        return True

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            transaction = {}
            transaction["amount"] = -1 * (amount)
            transaction["description"] = description
            self.ledger.append(transaction)
            self.balance -= amount
            completed = True
        else:
            completed = False
        return completed

    def get_balance(self):
        return self.balance

    def transfer(self, amount, destination_category):
        if self.check_funds(amount):
            successful_transfer = True
            self.withdraw(amount, f"Transfer to {destination_category}")
            destination_category.deposit(amount, f"Transfer from {self}")
        else:
            successful_transfer = False
        return successful_transfer

    def check_funds(self,amount):
        if amount > self.balance:
            available = False
        else:
            available = True
        return available

def create_spend_chart(categories):
    bar_chart = ""
    return bar_chart
