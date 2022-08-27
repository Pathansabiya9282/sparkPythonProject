d=int(input("enter date"))
m=int(input("enter month:"))

if (d>=1 and d<=30) and (m==4 or m==6 or m==9 or m==11):
    print("date is valid")
elif(d>=1 and d<=31) and (m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12):
    print("date is valid")
elif(d>=1 and d>=28) and (m==2):
    print("date is valid")
elif d % 4 == 0:
    print("date is valid")
else:
    print("date is invalid")


