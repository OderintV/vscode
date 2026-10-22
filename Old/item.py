# Initialize variables
total_cost = 0.0
max_total = 1000
excess_item = 0
attempt_count = 0

# Input quantity for Type 1
print("Enter the quantity of Type 1 items being manufactured: ", end='')
quantity_type1 = int(input())
if quantity_type1 < 0:
    print("Error: Quantity cannot be negative. Please enter a valid quantity.", end='')
    quantity_type1 = int(input())

# Input quantity for Type 2
print("Enter the quantity of Type 2 items being manufactured: ", end='')
quantity_type2 = int(input())
if quantity_type2 < 0:
    print("Error: Quantity cannot be negative. Please enter a valid quantity.", end='')
    quantity_type2 = int(input())

# Input quantity for Type 3
print("Enter the quantity of Type 3 items being manufactured: ", end='')
quantity_type3 = int(input())
if quantity_type3 < 0:
    print("Error: Quantity cannot be negative. Please enter a valid quantity.", end='')
    quantity_type3 = int(input())

# Calculate total quantity and validate
total_quantity = quantity_type1 + quantity_type2 + quantity_type3
while total_quantity > max_total:
    print("Error: Total quantity (", total_quantity, ") exceeds the maximum limit of ", max_total, ".", end='')
    attempt_count = attempt_count + 1
    if attempt_count > 3:
        print("Error: Too many attempts. Program terminated.")
        break

    if quantity_type1 > 0 and (quantity_type1 > quantity_type2 and quantity_type1 > quantity_type3):
        excess_item = 1
        print("Please re-enter the quantity of Type 1 items: ", end='')
        quantity_type1 = int(input())
        if quantity_type1 < 0:
            print("Error: Quantity cannot be negative. Please enter a valid quantity.", end='')
            quantity_type1 = int(input())
    else:
        if quantity_type2 > 0 and (quantity_type2 > quantity_type1 and quantity_type2 > quantity_type3):
            excess_item = 2
            print("Please re-enter the quantity of Type 2 items: ", end='')
            quantity_type2 = int(input())
            if quantity_type2 < 0:
                print("Error: Quantity cannot be negative. Please enter a valid quantity.", end='')
                quantity_type2 = int(input())
        else:
            if quantity_type3 > 0:
                excess_item = 3
                print("Please re-enter the quantity of Type 3 items: ", end='')
                quantity_type3 = int(input())
                if quantity_type3 < 0:
                    print("Error: Quantity cannot be negative. Please enter a valid quantity.", end='')
                    quantity_type3 = int(input())
    total_quantity = quantity_type1 + quantity_type2 + quantity_type3

# Print details of quantities
print("Manufactured Quantities:")
print("Type 1 items:", quantity_type1)
print("Type 2 items:", quantity_type2)
print("Type 3 items:", quantity_type3)
print("Total quantity:", total_quantity)

# Input parts cost for each item type
print("Enter the parts cost for Type 1 items: $", end='')
parts_cost_type1 = float(input())
if parts_cost_type1 < 0:
    print("Error: Parts cost cannot be negative. Please enter a valid cost.", end='')
    parts_cost_type1 = float(input())

print("Enter the parts cost for Type 2 items: $", end='')
parts_cost_type2 = float(input())
if parts_cost_type2 < 0:
    print("Error: Parts cost cannot be negative. Please enter a valid cost.", end='')
    parts_cost_type2 = float(input())

print("Enter the parts cost for Type 3 items: $", end='')
parts_cost_type3 = float(input())
if parts_cost_type3 < 0:
    print("Error: Parts cost cannot be negative. Please enter a valid cost.", end='')
    parts_cost_type3 = float(input())

# Calculate item costs based on type, quantity, and individual parts cost
item_cost_type1 = parts_cost_type1 * quantity_type1
item_cost_type2 = (parts_cost_type2 + 1.5) * quantity_type2
item_cost_type3 = (parts_cost_type3 + 5.0) * quantity_type3

# Calculate total cost
total_cost = item_cost_type1 + item_cost_type2 + item_cost_type3

# Calculate and output average cost
average_cost = total_cost / total_quantity
print("Total cost for all items: $", total_cost)
print("Average item cost per day (based on", total_quantity, "items): $", average_cost)