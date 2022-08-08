"""Read the four values corresponding to the x and y axes of two points in the plane, p1 (x1, y1) and p2 (x2, y2) and calculate the distance between them, showing f
our decimal places after the comma, according to the formula:

Distance =

Input
The input file contains two l
ines of data. The first one contains
 two double values: x1 y1 and the second one also
  contains two double values with one digit after
   the decimal point: x2 y2."""
import math


#p1 = x1y1
import math

x1, y1 = list(map(float, input().split()))
x2, y2 = list(map(float, input().split()))
distance = math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
print(f'{distance:0.4f}')