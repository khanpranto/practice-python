import random
n = 20
guess_number = int(n*random.random())+1
guess = 0
while guess != guess_number:
    guess = int(input("Enter your new number: "))
    if guess > 0:
        if guess < guess_number:
                        print("Number is too small")
        elif guess > guess_number:
                        print("Number is bigger ")
    else:
        print("You give up")
        break
else:
    print("You have made it")
