
def validate_units(unit):
    if not unit.isdigit():
        return False

    return True


def calculate_charge_foreach(unit):
    small_tier = 0
    medium_tier = 0
    large_tier = 0

    if unit <= 50:
        small_tier = unit * 0.50

    elif unit <= 150:
        small_tier = 50 * 0.50
        medium_tier = (unit - 50) * 0.75

    else:
        small_tier = 50 * 0.50
        medium_tier = 100 * 0.75
        large_tier = (unit - 150) * 1.20

    return small_tier, medium_tier, large_tier


def calculate_total_bill(unit, service_fee=0):
    small, medium, large = calculate_charge_foreach(unit)
    return small + medium + large + service_fee


def generate_billing_summary(unit, service_fee=0):
    small, medium, large = calculate_charge_foreach(unit)
    total = calculate_total_bill(unit, service_fee)

    print("\n===== ELECTRICITY BILL SUMMARY =====")
    print(f"Units consumed:       {unit}")
    print(f"First 50 units:       {small:.2f} Birr")
    print(f"Next 100 units:       {medium:.2f} Birr")
    print(f"Above 150 units:      {large:.2f} Birr")
    print(f"Service fee:          {service_fee:.2f} Birr")
    print("------------------------------------")
    print(f"Total bill:           {total:.2f} Birr")
    print("====================================")


units = input("Enter electricity units consumed: ")

if validate_units(units):
    units = int(units)
    generate_billing_summary(units, service_fee=10)
else:
    print("Invalid input. Enter a non-negative whole number.")
