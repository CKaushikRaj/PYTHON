sp = int(input("Enter the selling price of an item: "))
cp = int(input("Enter the cost price of an item: "))
if sp > cp :
 profit = sp - cp
 print(profit)
elif cp > sp :
 loss = cp - sp
 print(loss)
else :
 print("Neither profit nor loss") 