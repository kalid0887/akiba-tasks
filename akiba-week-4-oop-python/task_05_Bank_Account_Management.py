class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount

        return self.balance

    def display_balance(self):
        print(f"Owner: {self.owner}")
        print(f"Balance: {self.balance}")

account1 = BankAccount("Kalid", 2000)
account2 = BankAccount("Ahmed", 5000)

account1.deposit(500)
account1.withdraw(300)

account2.deposit(1000)
account2.withdraw(2000)

account1.display_balance()
account2.display_balance()