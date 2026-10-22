# good for small array
arr = [10, 20, 30, 40, 50]

try:
    a = int(input("Enter the index of the element you want to access: "))
    index = arr.index(a)
    print(f"index found at: {index}")
except ValueError:
    print("ValueError: The value is not in the list.")

