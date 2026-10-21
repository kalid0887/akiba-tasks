
OPENING_BALANCE = 2000.00
DAILY_WITHDRAWAL_LIMIT = 3000.00

balance = OPENING_BALANCE
total_deposited = 0.0
total_withdrawn = 0.0
daily_withdrawn = 0.0

transactions = []


def deposit_money(amount):
    global balance, total_deposited

    if amount <= 0:
        print("Please enter a positive amount.")
        return False

    balance += amount
    total_deposited += amount

    record_transaction("deposit", amount)
    print(f"Successfully deposited {amount:.2f} ETB")
    return True


def withdraw_money(amount):
    global balance, total_withdrawn, daily_withdrawn

    if amount <= 0:
        print("Please enter a positive amount.")
        return False

    if amount > balance:
        print("Insufficient balance.")
        return False

    remaining_limit = DAILY_WITHDRAWAL_LIMIT - daily_withdrawn

    if amount > remaining_limit:
        print(f"Daily withdrawal limit exceeded.")
        print(f"Remaining limit: {remaining_limit:.2f} ETB")
        return False

    balance -= amount
    total_withdrawn += amount
    daily_withdrawn += amount

    record_transaction("withdrawal", amount)
    print(f"Successfully withdrew {amount:.2f} ETB")
    return True


def check_balance():
    print(f"Current balance: {balance:.2f} ETB")
    return balance


def record_transaction(transaction_type, amount):
    transaction = {
        "type": transaction_type,
        "amount": amount,
        "balance_after": balance
    }

    transactions.append(transaction)


def transaction_summary():
    print("\n===== TRANSACTION SUMMARY =====")
    print(f"Opening balance: {OPENING_BALANCE:.2f} ETB")
    print(f"Total deposited: {total_deposited:.2f} ETB")
    print(f"Total withdrawn: {total_withdrawn:.2f} ETB")
    print(f"Final balance: {balance:.2f} ETB")
    print(f"Withdrawn today: {daily_withdrawn:.2f} ETB")
    print(f"Remaining daily limit: "
          f"{DAILY_WITHDRAWAL_LIMIT - daily_withdrawn:.2f} ETB")


def transaction_history():
    print("\n===== TRANSACTION HISTORY =====")

    if not transactions:
        print("No successful transactions yet.")
        return

    for index, transaction in enumerate(transactions, start=1):
        print(f"\nTransaction {index}")
        print(f"Type: {transaction['type']}")
        print(f"Amount: {transaction['amount']:.2f} ETB")
        print(f"Balance after: {transaction['balance_after']:.2f} ETB")


while True:
    print("\n===== BANK PROCESSOR =====")
    print("1. Deposit money")
    print("2. Withdraw money")
    print("3. Check balance")
    print("4. Transaction summary")
    print("5. Transaction history")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        try:
            amount = float(input("Enter deposit amount: "))
            deposit_money(amount)
        except ValueError:
            print("Please enter a valid number.")

    elif choice == "2":
        try:
            amount = float(input("Enter withdrawal amount: "))
            withdraw_money(amount)
        except ValueError:
            print("Please enter a valid number.")

    elif choice == "3":
        check_balance()

    elif choice == "4":
        transaction_summary()

    elif choice == "5":
        transaction_history()

    elif choice == "6":
        print("Thank you for using our bank processor.")
        break

    else:
        print("Invalid option. Please choose 1-6.")
