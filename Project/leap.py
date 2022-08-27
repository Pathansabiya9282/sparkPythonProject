days=int(input("how many days in leap year"))


if days == 366:
    print(" you have cleared first level")
    m = int(input("What month has an extra day in leap year?"))
    if m == 2:
        print(" Congratulations !!You have cleared the test ")
    else:
        print(" You have failed the test ")
else:
    print("Your input is wrong, please try again.")









