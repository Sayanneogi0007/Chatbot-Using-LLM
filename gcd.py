n1=int(input("enter 1st number :"))
n2=int(input("entter 2nd number :"))
if n1<n2:
    s=n1
else:
    s=n2
for i in range(1,s+1):
    if(n1%i==0) and (n2%i==0):
        gcd=i
print("G.C.D ",gcd)
    