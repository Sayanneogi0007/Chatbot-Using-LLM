n=int(input("ENTER THE NUMBER ::"))
c=n
arm=0
while(n>0):
    r=n%10
    arm=(r*r*r)+arm
    n=n//10
if(c==arm):
        print("IT IS A AMNSTRONG NUMBER ")
else:
        print("IT IS NOT A AMNSTRONG NUMBER ")