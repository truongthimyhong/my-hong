# dung for in range
a=[[i,i*8] for i in range(1,5)]
print(a)
#dung list()
a=list("hong123")
print(a) #out put cac phan tu cua a
#tim phan tu cos nam trong list hay khong
a=[1,2,3,4]
b= 1 in a
print(b)#true
c= 5 in a
print(c)#false
#ma tran in ra nhieu cai
a=[[1,2,3],[4,5,6]]
print(a[0])# phan tu 1
print(a[1])#phan tu 2
# list duoc dat trong dau [], cac phan tu cach  nhau boi dau "," 
#vi tri bat dau tu 0, ket thuc n-1
# toan tu
a=[1,2]
b=a+[4,5]# cong voi mot list khac
print(b)
# nhan
d=a*2
print(d)   # output ra 2 cai a
#khong nhan chuoi voi chuoi