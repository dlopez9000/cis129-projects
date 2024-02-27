# Darlene Lopez
# 2/26/2024
# program will keep track of bottle collections from a grocery store for seven days

# Step 1: Declare variables below
total_bottles = 0  # This variable will store the accumulated bottle values
counter = 1  # This variable will control the loop
today_bottles = 0  # This variable will store the number of bottles returned on a day
total_payout = 0  # This variable will store the calculated value of totalBottles times .10
keep_going = "y"  # This variable will be used to run the program again

# Step 3: Loop to run program again
while keep_going.lower() == "y":
    # Step 2: Code to set value of variables
    total_bottles = 0  # Reset total_bottles for each new week
    counter = 1  # Reset counter for each new week

    # Loop to collect bottles for each day of the week
    while counter <= 7:
        print("Enter number of bottles returned for day #",counter, ":")
        today_bottles = int(input())
        total_bottles += today_bottles
        counter += 1

    total_payout = total_bottles * 0.10
    print("The total number of bottles collected is", total_bottles)
    print("Total Payout for the week " " $ ", total_payout)

    keep_going = input("Do you want to enter another week’s worth of data? (Enter y or n): ")

# Step 6: printInfo code
print("The total number of bottles collected is", total_bottles)
print("Total Payout for the week " " $ ", total_payout)
