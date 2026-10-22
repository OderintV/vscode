# Searching algos

# linear search - unsorted data
# O(1) or O(n)
def linear_search(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1

def linear_search(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1

# binary search
# sorted data
# direct access to data (list)
# O(log₂ n) complexity - double the data, one step added
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid  # target found
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1  # target not found
 
# bubble sort
# O(n^2)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# insertion sort
# O(n^2)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > current:
            arr[j + 1] = arr[j]  # Shift elements right
            j -= 1
        arr[j + 1] = current

    
# ADT
def push(stack, item):
    stack.append(item)
def enqueue(queue, item):
    queue.append(item)
def insert_at_start(head, item):
    new_node = Node(item)
    new_node.next = head
    return new_node  # new head
def pop(stack):
    if stack:
        return stack.pop()
    return None
def dequeue(queue):
    if queue:
        return queue.pop(0)
    return None
