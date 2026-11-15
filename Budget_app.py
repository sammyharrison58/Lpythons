class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item["amount"]
        return balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = self.name.center(30, "*") + "\n"
        items = ""
        for item in self.ledger:
            description = item["description"][:23].ljust(23)
            amount = f"{item['amount']:.2f}".rjust(7)
            items += f"{description}{amount}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


def create_spend_chart(categories):
    # Calculate total spent and spent per category
    spent = []
    total_spent = 0

    for category in categories:
        category_spent = 0
        for item in category.ledger:
            if item["amount"] < 0:
                category_spent += abs(item["amount"])
        spent.append(category_spent)
        total_spent += category_spent

    # Calculate percentages (rounded down to nearest 10)
    percentages = []
    for amount in spent:
        percentage = (amount / total_spent) * 100
        percentages.append(int(percentage // 10) * 10)

    # Build the chart
    chart = "Percentage spent by category\n"

    for i in range(100, -1, -10):
        chart += str(i).rjust(3) + "|"
        for percent in percentages:
            if percent >= i:
                chart += " o "
            else:
                chart += "   "
        chart += " \n"

    # Dashed line
    chart += "    " + "-" * (3 * len(categories) + 1) + "\n"

    # Category names (vertical)
    max_length = max(len(category.name) for category in categories)
    for i in range(max_length):
        chart += "    "
        for category in categories:
            if i < len(category.name):
                chart += " " + category.name[i] + " "
            else:
                chart += "   "
        chart += " \n"

    return chart.rstrip("\n")