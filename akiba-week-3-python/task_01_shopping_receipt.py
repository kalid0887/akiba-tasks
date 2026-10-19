
items = [
    {"name": "Notebook", "price": 80, "quantity": 3},
    {"name": "Pen", "price": 15, "quantity": 5},
    {"name": "laptop", "price": 300, "quantity": 3}
]

tax_rate = 0.15


def calculate_subtotal(items):
    total_price = 0

    for item in items:
        total_price += item["price"] * item["quantity"]

    return total_price


def calculate_discount(subtotal):
    if subtotal <= 1000:
        return subtotal
    elif subtotal <= 2999:
        return subtotal * 0.95
    else:
        return subtotal * 0.9


def calculate_tax(amount, tax_rate):
    tax = amount * tax_rate
    return tax


def generate_receipt(items, tax_rate):
    subtotal = calculate_subtotal(items)
    discounted_total = calculate_discount(subtotal)
    discount_amount = subtotal - discounted_total
    tax = calculate_tax(discounted_total, tax_rate)
    final_total = discounted_total + tax

    print("=" * 35)
    print("          SHOPPING RECEIPT")
    print("=" * 35)

    for item in items:
        item_total = item["price"] * item["quantity"]
        print(f"{item['name']}: {item['quantity']} x "
              f"{item['price']} = {item_total}")

    print("-" * 35)
    print(f"Subtotal:        {subtotal:.2f}")
    print(f"Discount:       -{discount_amount:.2f}")
    print(f"After discount:  {discounted_total:.2f}")
    print(f"Tax (15%):       {tax:.2f}")
    print("-" * 35)
    print(f"Final total:     {final_total:.2f}")
    print("=" * 35)


generate_receipt(items, tax_rate)
