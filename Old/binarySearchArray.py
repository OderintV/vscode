def binary_search(arr, target):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target: 
            low = mid + 1   
        else:
            high = mid - 1
    return -1  
arr = []
target = int(input("enter: "))
if binary_search(arr, target) == -1:
    print("Record exists")
else:
    print(f"Record exists at position {binary_search(arr,target) +1} in array")
