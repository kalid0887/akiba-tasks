customer_name = input("what is your name dear customer? ").upper()
product_name = input("what is the product name? ")
price = float(input("please enter the price"))
quantity = int(input("enter the quantity:  "))

print("\n========================================\n")
print("HAPPY FASHION RECEIPT")
print("========================================\n")

print(f"Customer Name: {customer_name}")
print("product      price       qty")
print("-------------------------------------------")
print(f"{product_name}      {price}     {quantity}")
print(f"\n Total:  {quantity * price}")

print("\n thank you for visiting us")
print("\n\n========================================\n\n")