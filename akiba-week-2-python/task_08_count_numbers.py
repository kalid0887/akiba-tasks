N = int(input("enter the positive number N: "))
sum = 0
odd = 0
even = 0
for n in range(N):
    sum = sum + n 
    if n % 2 == 0:
        even += 1
    else:
        odd += 1
    n +=1

print(f"the sum of numbers is {sum}")

print(f"number of odd numbers is {odd}")
print(f"number of even numbers is {even}")