import math
a=float(input("nhap a="))
b=float(input("nhap b="))
c=float(input("nhap c="))
p=float((a+b+c)/2)
s=math.sqrt(p*(p-a)*(p-b)*(p-c))
if (a+b)>c and (a+c)>b and (b+c)>a:
    print("dien tich=",round(s,3),sep="")
else: print("khong hop le")