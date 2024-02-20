# Module 4 Lab-4
# Darlene Lopez
# 2/19/2024
# This program is calculating bonuses for both the store and employees based on monthly sales

# declare local variables

monthlySales = 0  # monthly sales amount
storeAmount = 0  # store bonus amount
empAmount = 0  # employee bonus amount
salesIncrease = 0  # percent of sales increase
prompt = "Enter the monthly sales amount: " 


monthlySales = float(input(prompt))


if monthlySales >= 110000:
    storeAmount = 6000
elif monthlySales >= 100000:
    storeAmount = 5000
elif monthlySales >= 90000:
    storeAmount = 4000
elif monthlySales >= 80000:
    storeAmount = 3000
else:
    storeAmount = 0


salesIncrease = float(input("Enter the percent increase in sales: "))
salesIncrease = salesIncrease / 100


if salesIncrease >= 0.05:
    empAmount = 75
elif salesIncrease >= 0.04:
    empAmount = 50
elif salesIncrease >= 0.03:
    empAmount = 40
else:
    empAmount = 0


print("The store bonus amount is $", storeAmount)
print("The employee bonus amount is $", empAmount)

if (storeAmount == 6000) and (empAmount == 75):
    print("Congratulations! You qualify for the maximum store bonus and employee bonus.")
