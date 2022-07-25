print("Wellcome to Bank of Pranto")
restart = ("Y")
balance = 100
chance = 3
while chance >= 0:
    pin = int(input("Enter your pin: "))
    if pin == (1234):
        print("You have enter the pin correctly: \n",)
        while restart not in('n','N','No','no'):
            print("please pres 1 for your balance : \n")
            print("please press 2 for make a withdrw : \n")
            print("please press 3 for pay in: \n")
            print("please press 4 for return the card: \n")
            option = int(input("what option would you like to chose\n"))
            if option == 1:
                print("your current balance is:", balance,'\n')
                restart = input('would you like to go back?')
                if restart in('n','N','No','no'):
                    print("thank you")
                    break
            elif option == 2:
                #option2 ='Y'
                withdrawl = float(input("how much do you want to withdraw\n"))
                if withdrawl in ['10','20','30','40','50','60','70','80','90','100']:
                    balance = balance - withdrawl
                    print('your current balance is :',balance)
                    restart = input("would you like to go back?\n")
                    if restart in('n','N','No','no'):
                        print("thank you")
                        break
                    elif withdrawl not in ['10','20','30','40','50','60','70','80','90','100']:
                        print("Enter the correct ammount : ")
                        restart = 'Y'
                    elif withdrawl == 1:
                        print("Enter the correct value: ")

            elif option == 3:
                pay_in = int(input("how much money do you want to deposit: \n"))
                balance = balance + pay_in
                restart = input("would you like to go back\n")
                if restart in('n','N','No','no'):
                    print("thank you")
                    break
            elif option == 4:
                print("please wait for the card\n")
                print("thank you for your service")
                break
            else:
                print("enter the correct number.")
                restart = 'Y'
    elif pin != (1234):
        print("incoreect pin")
        chance = chance - 1
        if chance == 0:
            print("no more try")
            break




