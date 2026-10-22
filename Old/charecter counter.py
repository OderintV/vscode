s = input("Enter a string: ")

digits = 0
alphabets = 0
special = 0

for char in s:
    if char.isdigit():
        digits += 1
    elif char.isalpha():
        alphabets += 1
    else:
        special += 1

print("Digits:", digits)
print("Alphabets:", alphabets)
print("Special characters:", special)