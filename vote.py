a = int(input("Enter age: "))
if a>=18:
 id = input("Voter id :")
if a >=18 and id == "yes" :
    print("Eligible to vote")
elif a >=18 and id == "no":
    print("Apply for voter id")
else:
    print("Not eligible")

  