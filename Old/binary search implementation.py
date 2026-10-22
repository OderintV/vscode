n = float(input("Enter number to find "))
arr = [5.6, 11.5, 20.8,35.4,43.1,52.4,66.6,78.9,80.0,95.5]

def binary_search(arr, n):
    low = 0
    high = len(arr) -1
    while low<= high:
        mid = (low + high)//2
        if arr[mid] == n:
            return mid
        elif arr[mid] < n:
            low = mid + 1
        else:
            high = mid -1
    return -1

if binary_search(arr,n) == -1:
    print("not found")
else:
    print("found")
