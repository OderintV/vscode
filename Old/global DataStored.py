global DataStored
global NumberItems
DataStored = []
NumberItems = len(DataStored)

def Initialise():
    while True:
        try:
            while True:
                quantity = int(input("Enter quantity of numbers to be entered"))
                if quantity > 0 and quantity < 21:
                    break
        except ValueError:
            pass
        else:
            break
    for _ in range(quantity):
        while True:
            num = int(input("Enter number between 1 and 20 inclusive"))
            if num > 0 and num < 21:
                DataStored.append(num)
            else:
                continue
    
def main():
    NumberItems = 0
    Initialise()
    for i in range(NumberItems):
        print(DataStored[i])
    
    