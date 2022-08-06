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
            right_alignment = str(format(float(item["amount"]), '.2f'))[0:7]
            body += f"{left_alignment : <23}{right_alignment : >7}\n"
        total_amt = format(float(self.balance), '.2f')
        total = f"Total: {total_amt}"
        display = str(header)+str(body)+total
        return display

    def deposit(self, amount, description=""):
        transaction = {}
        transaction["amount"] = amount
        transaction["description"] = description
        self.ledger.append(transaction)
        self.balance += amount
        return True

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            transaction = {}
            transaction["amount"] = -1 * amount
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

    def check_funds(self, amount):
        if amount > self.balance:
            available = False
        else:
            available = True
        return available


def create_spend_chart(category_list):
    data = {"Total": 0}
    label_max = 0
    for single_category in category_list:
        # Determines and stores length of longest category name for labeling
        length = len(single_category.name)
        if length > label_max:
            label_max = int(length)

        # Create Key:Value pair of Category:Expenses
        data[single_category.name] = 0

        # Sum of withdrawals only per Category
        for transaction in single_category.ledger:
            if transaction["amount"]<0:
                data[single_category.name] += abs(transaction["amount"])
                data["Total"] += abs(transaction["amount"])

    # Normalize withdrawals to % of total expenses
    total = float(data["Total"])
    for single_category in data:
        data[single_category] = int((float(data[single_category])/total)*100)

    # Delete unneeded key in preparation for parsing
    data.pop("Total")

    # Graph Title
    title = "Percentage spent by category\n"

    # Graph Data
    graph = ""
    num = 110
    while num>0:
        num -= 10
        graph += f"{num : >3}| "
        for single_category in data.keys():
            if data[single_category] >= num:
                graph += "o  "
            else:
                graph += "   "
        graph += "\n"

    # X-axis bar line
    separator = "    -" + "---"*len(category_list)

    char = 0
    label = ""
    while char < label_max:
        label += "\n     "
        for single_category in data.keys():
            try:
                if not single_category[char] == "":
                    label += single_category[char] + "  "
            except IndexError:
                label += "   "
        char += 1

    chart = title + graph + separator + label
    return chart
