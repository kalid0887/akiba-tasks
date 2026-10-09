number = int(input("enter the number: "))

match_found = False
if number < 2:
    print("Neither prime nor composite")

devisor = 2
if number > 0 and number != 1:
    while devisor < number:
        if number % devisor == 0:
            print("composite number")            
            match_found = True
            break
        devisor += 1
        
    if not match_found:#""" and number % (devisor-1) != 0"""
        print("prime")
    