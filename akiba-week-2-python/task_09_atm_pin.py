correctPin = 1234


count = 0
correct = True
while count < 3:
    pin = int(input("enter the pin: "))
    if pin != correctPin:
        count += 1
        print(f"please try again!, you have left {3-count} trials")
        
    else:
        print("you are succesfully loged in!")
        break
