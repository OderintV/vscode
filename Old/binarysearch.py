# binary search can only be used in a sorted array
# good for searching in a big array
# O(log n) time complexity 

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

