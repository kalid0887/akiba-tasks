number = int(input("enter the number: "))



digits = [int(d) for d in str(abs(number))]

reversed_numbers = digits[::-1]
if len(str(abs(number))) == 1:
    print("palindrome")
elif number <= 0:
    print("not palindrome")
elif reversed_numbers == digits:
    print("palindrome")
else:
    print("not palindrome")
