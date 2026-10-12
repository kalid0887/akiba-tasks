# number = int(input("enter the number: "))



# digits = [int(d) for d in str(abs(number))]

# reversed_numbers = digits[::-1]
# if len(str(abs(number))) == 1:
#     print("palindrome")
# elif number <= 0:
#     print("not palindrome")
# elif reversed_numbers == digits:
#     print("palindrome")
# else:
#     print("not palindrome")

number = int(input("enter the number: "))
original = number
reversedNumber = 0

count = 0
while number > 0:
    digit = number % 10
    number = number //10
    if count == 0:
        reversedNumber = digit
    else:
        reversedNumber = (reversedNumber * 10) + digit
    count += 1


if number < 0:
    print("not palindrom")

if original == reversedNumber:
    print("palindrome")
else:
    print("not palindrome")

# print(reversedNumber)
# print(number)