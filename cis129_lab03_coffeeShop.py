# Coffee shop program showing coffee shop name and items
print('***************************************')
print("Puppuccino Cafe")
print("Number of coffees bought?")
num_coffee = int(input())
print("Number of muffins bought?")
num_muffins = int(input())
print('***************************************')
print()
print()
print('***************************************')

# Calculate the subtotal
coffee_price = 5.00
muffin_price = 4.00
coffee_subtotal = num_coffee * coffee_price
muffin_subtotal = num_muffins * muffin_price
total_subtotal = coffee_subtotal + muffin_subtotal
subtotal = (num_coffee * coffee_price) + (num_muffins * muffin_price)


# Calculate the tax
tax_rate = 0.06
tax_amount = subtotal * tax_rate
# Calculate the total
total = subtotal + tax_amount

# Display the items purchased and the total amount
print("Puppuccino Cafe Receipt")
print(num_coffee, "Coffee at $5 each:", "$", coffee_subtotal )
print(num_muffins, "Muffin at $4 each:", "$", muffin_subtotal )

# Display the subtotal, tax, and total to the customer
print("6% Tax: $", tax_amount)
print('---------')
print("Total: $", total)
print('***************************************')
