## Inputs we need from the user
# Total rent
# Total food ordered for snacking
# Electricity units spend
# Charge per unit
# persons live in room

## Output
# Total amount you've to pay is


rent = int(input("Total Rent of room/hostel : "))
food = int(input("Total amount of ordered food : "))
electricity_units = int(input("No. of units spended : "))
charge_per_unit = int(input("Charge per unit on electricity : "))
members = int(input("No. of persons live in room/hostel : "))

total_bill = (electricity_units * charge_per_unit)

total_amount = (total_bill + rent + food) // members

print("Each have to pay the amount of ", total_amount, "in room.")