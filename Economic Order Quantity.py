# Economic Order Quantity (EOQ)

demand = int(input('Enter Your Demand: '))
ordering_cost = int(input("Ordering Cost: "))
holding_cost = int(input("Holding Cost: "))

# Calculate the Total Economic Order Quantity (EOQ)
total_economic = ((2 * demand * ordering_cost) / holding_cost) ** 0.5

print("Total Economic Quantity: ", total_economic)
