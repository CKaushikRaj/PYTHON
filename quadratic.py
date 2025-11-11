a = int(input("Enter the coefficient of x^2 : "))
b = int(input("Enter the coefficient of x : "))
c = int(input("Enter the constant value : "))
discriminant = (b * b) - 4 * (a * c)
print(discriminant)
if discriminant > 0:
    print("The equation has two root.")
elif discriminant == 0:
    print("The equation has one real root.")
else:
    print("The equation has two distinct complex roots.")