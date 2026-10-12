numbers = []
index = 0
odd = 0
even = 0
sum = 0
greatest = 0
smallest = 10000
sum = 0
while len(numbers) < 10:
    index += 1
    number = int(input(f"enter the index: {index} number: "))
    if number > greatest:
        greatest = number
    if number < smallest:
        smallest = number
    sum = sum + number
    average = sum / 10 # we can use len(numbers)
    numbers.append(number)

    if number % 2 == 0:
            even += 1
    else:
        odd += 1

print(f"the sum of numbers is {sum}")

print(f"number of odd numbers is {odd}")
print(f"number of even numbers is {even}")
print(f"the smallest number is {smallest}")

print(f"the greatest number is {greatest}")
print(f"the averages of numbers is {average}")