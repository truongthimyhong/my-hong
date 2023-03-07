m1=float(input("m1="))
m2=float(input("m2="))
m3=float(input("m3="))
s=float(input("s="))
if s<100: print("Phai tra=",s*m1,sep="")
elif 100<s<=150:
    v=s-100
    print("Phai tra=",100*m1+v*m2,sep="")
else:
    vv=s-150
    print("Phai tra=",100*m1+50*m2+vv*m3,sep="")
