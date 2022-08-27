a,b,c=[int(x) for x in input("enter value of triangle:").split()]

if a+b>=c and b+c>=a and c+a>=b:
    print("triangle is valid")
else:
    print("triangle is invalid")