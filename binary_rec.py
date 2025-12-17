def binary_search_rec(arr,low,high,x):
    if high >= low:
        mid = low + (high - low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search_rec(arr,low,mid-1,x)
        else:
            return binary_search_rec(arr,mid+1,high,x)
    else:
        return -1
arr =[int(x) for x in input("Enter the numbers seperated ny space :").split()]

x =int(input("Enter the number:"))

res = binary_search_rec(arr,0,len(arr)-1,x)
if res != -1:
    print("Element",x, "found at index", res)
else :
    print("Element not found in the array")
