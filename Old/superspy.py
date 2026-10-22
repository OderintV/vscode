# superspy number

def superspy_no(n):
    total = 0
    s = str(n)
    length = len(s)
    for i in range(length):
        total += int(s[i])
    if length == total:
        return True
    return False

n = int(input("Enter a number: "))
print(superspy_no(n))


