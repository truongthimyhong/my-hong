import math
a=float(input("nhap a="))
b=float(input("nhap b="))
c=float(input("nhap c="))
s=float((a+b+c)/2)
dt=float(math.sqrt(s*(s-a)*(s-b)*(s-c)))
print("dien tich=",dt)