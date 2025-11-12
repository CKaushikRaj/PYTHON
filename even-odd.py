a = int(input("Enter a number :"))
if a % 2 == 0 and a > 0:
    print("EVEN & POSITIVE")
elif a < 0 :
    print("NEGATIVE")
elif a % 2 != 0 and a > 0:
    print("ODD & POSITIVE")
else :
    print("enter valid input") 