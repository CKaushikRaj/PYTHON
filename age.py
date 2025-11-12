age = int(input("Enter age(in years):"))
if age<=0 :
    print("Person is baby")
elif age<=13:
    print("Person is child")
elif age<=19:
    print("Teenage")
elif age<=27:
    print("Youth")
elif age<=35:
    print("Middle age")
elif age<=59:
    print("Retirement age")
elif age>=60:
    print("Old age")