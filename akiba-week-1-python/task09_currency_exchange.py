exchange_rate = 150

usd_amount = float(input("enter amount USD you want to convert to ETB"))
etb_amount = usd_amount * exchange_rate

print("\n========================================\n")
print("\t CURRENCY EXCHANGE\t")
print("========================================\n")


print(f"USD Amount: {usd_amount}")
print(f"exchange rate: 1 USD = {exchange_rate}")

print(f"ETB amount: {etb_amount}")
