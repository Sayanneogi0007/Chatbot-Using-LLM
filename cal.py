n1=int(input("enter first number ::"))
n2=int(input("enter second number ::"))
print("enter (1) for +")
print("enter (2) for -")
print("enter (3) for *")
print("enter (4) for /")
print("enter (5) for %")
x=int(input("ENTER WHICH OPERATION YOU WANT TO DO ::"))
match x:
    case 1:
        a=n1+n2
        print("ANS",a)
    case 2:
        a=n1-n2
        print("ANS",a)
    case 3:
        a=n1*n2
        print("ANS",a)
    case 4:
        a=n1//n2
        print("ANS",a)
    case 5:
        a=n1%n2
        print("ANS",a)