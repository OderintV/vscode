total = 0
counter = 0

while counter < 1000:
    try:
        while True:
            item_type = int(input("enter type: "))
            cost = float(input("enter cost: "))
            number = int(input("how many to produce: "))

            if counter + number > 1000:
                print(f"Only {1000 - counter} items can be produced to reach 1000.")
                continue  

            if item_type == 1:
                item_cost = cost * 1.5
            elif item_type == 2:
                item_cost = cost * 2.5
            elif item_type == 3:
                item_cost = cost * 5.0
            else:
                print("Type should be 1, 2, or 3")
                continue

            print(f"Item costs {item_cost}")
            total += item_cost * number
            counter += number

            if counter == 1000:
                break

    except ValueError:
        print("Wrong input, enter numbers only.")
    except EOFError:
        print("\nEOF detected, exiting program.")
        exit()

print("Average cost per day:", total / 1000)
