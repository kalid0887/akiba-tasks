secretNumber = 32

found = False
count = 0
while found == False and count < 5:
    guessedNumber = int(input("guess a number: "))
    if guessedNumber == secretNumber:
        found = True
        print("congratulaions u got the secret number")
        break
    else:
        if guessedNumber < secretNumber:
            print(f"please try the number greater than {guessedNumber}")
        else:
            print(f"please try the number less than {guessedNumber}")
        count += 1


if count == 5:
    print("sorry you have used 5 chances but u cant get the number, see u next time")