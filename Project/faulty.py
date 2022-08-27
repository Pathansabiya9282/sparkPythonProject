a=int(input("enter number one:"))
b=int(input("enter number two:"))
opr=input("enter operator:")

if(a==45 and b==3 and opr=='*'):
    print("555")
elif(a==56 and b==9 and opr=='+'):
    print("77")
elif(a==56 and b==6 and opr=='/'):
    print("4")
elif opr=='+':
    print(a+b)
elif opr=='-':
    print(a-b)
elif opr=='*':
    print(a*b)
else:
    print("wrong")