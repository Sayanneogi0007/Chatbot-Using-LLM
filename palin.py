n=int(input("enter the number ::="))
c=n
s=0
while(n>0):
    r=n%10
    s=r+(s*10)
    n=n//10
    
if(s==c):
    print(":: IT IS A PALINDROM NUMBER ::")
else:
    print(":: IT IS NOT A PALINDROM NUMBER ::")