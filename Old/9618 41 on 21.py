
def Unknown(X, Y: int):
    if X<Y:
        print(X+Y)
        return (Unknown(X+1,Y)*2)
    elif X ==Y:
        return 1
    else:
        print(X+Y)
        return (Unknown(X-1,Y) // 2)



def IterativeUnkown(X,Y):
    Total = 1
    while X != Y:
        print(str(X+Y))
        if X<Y:
            X += 1
            Total = Total * 2
        else:
            X -= 1
            Total = int(Total/2)
            
    return Total
            
print("10 and 15")
print(Unknown(10, 15))
print("10 and 10")
print(Unknown(10, 10))
print("15 and 10")
print(Unknown(15, 10))

print("iterative now")
print("10 and 15")
print(IterativeUnkown(10, 15))
print("10 and 10")
print(IterativeUnkown(10, 10))
print("15 and 10")
print(IterativeUnkown(15, 10))

