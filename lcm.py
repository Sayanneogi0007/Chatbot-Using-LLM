n1=int(input("enter number 1  ::"))
n2=int(input("enter number 2  ::"))
if n1>n2:
    grater=n1
else:
    grater=n2
for i in range(1,grater+1):
    if(n1%i==0) and (n2%i==0):
        gcd=i
        break
grater+=1
