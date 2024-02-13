# Coffee shop program showing coffee shop name and items
print('***************************************')
print("Puppuccino Cafe")
print("Number of coffees bought?")
num_coffee = int(input())
print("Number of muffins bought?")
num_muffins = int(input())
print("Number of seapup donuts bought?")
num_donuts = int(input())
print("Number of iced lattes bought?")
num_lattes = int(input())
print('***************************************')
print()
print()
print('***************************************')

# Calculate the subtotal
coffee_price = 5.00
muffin_price = 4.00
donut_price = 3.00
latte_price = 5.00
coffee_subtotal = num_coffee * coffee_price
muffin_subtotal = num_muffins * muffin_price
donut_subtotal = num_donuts * donut_price
latte_subtotal = num_lattes * latte_price
total_subtotal = coffee_subtotal + muffin_subtotal + donut_subtotal + latte_subtotal
subtotal = (num_coffee * coffee_price) + (num_muffins * muffin_price) + (num_donuts * donut_price) + (num_lattes * latte_price)


# Calculate the tax
tax_rate = 0.06
tax_amount = subtotal * tax_rate
# Calculate the total
total = subtotal + tax_amount

# Display the items purchased and the total amount
print("Puppuccino Cafe Receipt")
print(num_coffee, "Coffees at $5 each:", "$", coffee_subtotal )
print(num_muffins, "Muffins at $4 each:", "$", muffin_subtotal )
print(num_donuts, "Seapup Donuts at $3 each:", "$", donut_subtotal )
print(num_lattes, "Iced Lattes at $5 each:", "$", latte_subtotal )
# Display the subtotal, tax, and total to the customer
print("6% Tax: $", tax_amount)
print('---------')
print("Total: $", total)
print('***************************************')
print("Thank You!")
print("𓆝 𓆟 𓆞 𓆝 𓆟")
