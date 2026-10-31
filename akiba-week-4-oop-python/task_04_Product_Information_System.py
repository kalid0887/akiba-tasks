class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"name: {self.name}, price: {self.price}, quantity: {self.quantity}"

    def total_value(self):
        return self.price * self.quantity



p1 = Product("notebook", 50, 3)
p2 = Product("pencil", 30, 7)
p3 = Product("pen", 40, 5)

print(f"{p1}, total price: {p1.total_value()}")

print(f"{p2}, total price: {p2.total_value()}")

print(f"{p3}, total price: {p3.total_value()}")

"""
The __str__() method defines a human-readable string 
representation of an object when it is printed.
"""