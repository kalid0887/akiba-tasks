
number = 123

def is_prime(number):
    if number < 2:
        return False

    divisor = 2

    while divisor < number:
        if number % divisor == 0:
            return False
        divisor += 1

    return True


def get_divisors(number):
    divisors = []

    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)

    return divisors


def sum_of_digits(number):
    total = 0

    while number > 0:
        digit = number % 10
        total += digit
        number = number // 10

    return total


def reverse_number(number):
    reversed_number = 0

    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number = number // 10

    return reversed_number


def is_even(number):
    return number % 2 == 0


def analyze_number(number):
    if is_even(number):
        print("The number is even")
    else:
        print("The number is odd")

    if is_prime(number):
        print("The number is prime")
    else:
        print("The number is not prime")

    print(f"The sum of the digits is {sum_of_digits(number)}")
    print(f"The reversed value is {reverse_number(number)}")
    print(f"Its divisors are {get_divisors(number)}")


analyze_number(number)
