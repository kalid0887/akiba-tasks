number =  4726
sum_of_dijit = 0

while number != 0:
    sum_of_dijit += number % 10
    number = number // 10
print(sum_of_dijit)