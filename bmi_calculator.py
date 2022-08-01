name = input()
weight = int(input("enter height:"))
height = int(input("enter height:"))

def BMI(name,weight,height):
    bmi = weight / (height ** 2)
    if(bmi<16):
       return "overweight",bmi
    else:
       return "not overweight",bmi

quote, bmi= BMI(name,height,weight)
print((bmi,quote))