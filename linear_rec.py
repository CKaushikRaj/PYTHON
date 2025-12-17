def linear_search_rec(arr , x , i=0):
    if i == len(arr):
        return -1
    if arr[i] == x:
        return i
    return linear_search_rec(arr , x ,i+1)

arr = [int(x) for x in input("Enter numbers separated by space: ").split()]
print(arr)

x = int(input("Enter the number :"))
res = linear_search_rec(arr,x)

if res != -1:
    print("Element", x, "found at index",res)
else:
    print("Element not found in the list")
