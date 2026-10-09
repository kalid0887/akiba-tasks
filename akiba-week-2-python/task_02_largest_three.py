num1 = float(input("enter the first number: "))
num2 = float(input("enter the second number: "))
num3 = float(input("enter the third number: "))

if num1 == num2 == num3:
    print("all three numbers are equal")
elif (num1 == num2) and num1 > num3:
    print(f"{num1} and {num2} are equal and they are greater than {num3}.")
elif (num1 == num3) and num1 > num2:
    print(f"{num1} and {num3} are equal and they are greater than {num2}.")
elif (num3 == num2) and num3 > num1:
    print(f"{num3} and {num2} are equal and they are greater than {num1}.")
elif num1 > num2 and num1 > num3:
    print(f"{num1} is the largest.")
elif num2 > num1 and num2 > num3:
    print(f"{num2} is the largest.")
elif num3 > num1 and num3 > num2:
    print(f"{num1} is the largest.")
else:
    print("please enter the correct formated number")