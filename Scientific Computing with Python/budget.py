class Category:
    def __init__(self, category_name=""):
        self.ledger = []
        self.balance = float(0.0)
        self.name = str(category_name.lower().capitalize())

    def __repr__(self):
        header = self.name.center(30, "*")
        body = "\n"
        for item in self.ledger:
            left_alignment = str(item["description"])[0:23]
            right_alignment = str(format(float(item["amount"]),'.2f'))[0:7]
            body += f"{left_alignment : <23}{right_alignment : >7}\n"
        total_amt= format(float(self.balance), '.2f')
        total = f"Total: {total_amt}"
        display = str(header)+str(body)+total
        return display

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
            self.withdraw(amount, f"Transfer to {destination_category.name}")
            destination_category.deposit(amount, f"Transfer from {self.name}")
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


def test():
    food = Category("Food")
    food.deposit(1000, "initial deposit")
    food.withdraw(10.15, "groceries")
    food.withdraw(15.89, "restaurant and more food for dessert")
    print(food,"\n")
    clothing = Category("Clothing")
    food.transfer(50, clothing)
    clothing.withdraw(25.55)
    clothing.withdraw(100)
    print(food)
    print(clothing)
    auto = Category("Auto")
    auto.deposit(1000, "initial deposit")
    auto.withdraw(15)
    print(auto)

    # print(food)
    # print(clothing)


def test_to_string():
    food = Category("Food")
    entertainment = Category("Entertainment")
    food.deposit(900, "deposit")
    food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
    food.transfer(20, entertainment)
    print(food)
    print("\nEXPECTED")
    print(
        f"*************Food*************\ndeposit                 900.00\nmilk, cereal, eggs, bac -45.67\nTransfer to Entertainme -20.00\nTotal: 834.33")

# test()
# test_to_string()
