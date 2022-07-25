number = int(input("enter the number:"))
factorial = 1
if number < 0:
    print("please enter positive number")
elif number == 0:
    print("Factorial is 1")
else:
    for i in range(1, number + 1):
        factorial = factorial * i
        print(factorial)
