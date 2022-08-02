#1+2+3+.....n
number = int(input("enter input for series one:"))
sum = 0

for i in range(1,number+1,1):
    sum = sum + i
print(sum, end=" ")

#here end use for print serially
#2+4+........+n jor songkha and jor ongkar jogfol

n = int(input("enter the number: "))
sum = 0
for i in range(2,n+1,2):
    print(i,end=" ")
    sum = sum +i
print(f"sumation of the series: {sum}")

