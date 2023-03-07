t=1
i=1
a=1
j=1
while j<=9:
    if  j <= 9 and i//9!=j and i%9!=0:
        g=t*a
        print(g,end=" ")
    elif i//9==j and i%9==0:#i chia 9 lấy phần nguyên bằng j: vd 18 chia 9 =2 khi j=2, xuống dòng
        g=t*a
        print(g)
        t=t+1
        j=j+1
        a=0
    i=i+1
    a=a+1
        
    