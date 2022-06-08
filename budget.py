class Category:

    def __init__(self, budcat):
        self.budgetCategory = budcat
        self.ledger = list()
        self.incomes = 0
        self.spents = 0

    def deposit(self, amount, description = ""):
        self.ledger.append({"amount": amount, "description": description})
        self.incomes += amount

    def get_balance(self):
        balance = 0
        for operation in self.ledger:
            balance += operation.get("amount", 0)            
        return balance

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True

    def withdraw(self, amount, description = ""):
        if self.check_funds(amount):
            self.ledger.append({"amount": (amount * -1), "description": description})
            self.spents += amount
            return True
        else:
            return False

    def transfer(self, amount, destination):
        destination_description = "Transfer to " + destination.budgetCategory
        source_description = "Transfer from " + self.budgetCategory
        if self.withdraw(amount, destination_description):
            destination.deposit(amount, source_description)
            return True
        else:
            return False

    def __repr__(self):
        repr_string = str()
        repr_string += "*" * (15 - int(len(self.budgetCategory)/2)) + self.budgetCategory + "*" * (15 - int(len(self.budgetCategory)/2)) + "\n"
        for operation in self.ledger:
            if len(operation.get("description", "")) <= 23:
                repr_string += operation.get("description", "") + " " * (23 - len(operation.get("description", "")))
            else:
                repr_string += operation.get("description", "")[:23]
            if len(str(int(operation.get("amount",0)))) < 4:
                repr_string += " " * (4 - len(str(int(operation.get("amount",0)))))
                repr_string += str('{0:.2f}'.format(operation.get("amount",0)))
                repr_string += "\n"
            else:
                repr_string += str('{0:.2f}'.format(operation.get("amount",0)))
                repr_string += "\n"
        repr_string += "Total: " + str('{0:.2f}'.format(self.get_balance()))
        
        return repr_string

def create_spend_chart(categories):
    ancho = len(categories)
    histogram = str()
    spents_percent = list()
    histogram += "Percentage spent by category\n"

    for category in categories:
        percent = int(category.spents / (category.incomes) * 100)
        if  (percent/10 - int(percent/10)) >= 0.5:
            percent = (int(percent/10) + 1) *10
        else:
            percent = int(percent/10) *10
        spents_percent.append(percent)
        # print("En la cat ", category.budgetCategory, " se gastó el ", percent, " porciento")

    for i in [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]:
        histogram += " " * (3 - len(str(i))) + str(i) + "|"
        for percent in spents_percent:
            if percent < i:
                histogram += "   "
            else:
                histogram += " o "
        histogram += "\n"

    histogram += " " * 4 + "---" * len(categories) + "-\n"
    
    # me falta imprimir los nombres en el histograma
    
    return histogram



food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)

print(create_spend_chart([food, clothing, auto]))