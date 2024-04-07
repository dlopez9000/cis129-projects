def format_check_protected_amount(amount):
    amount_str = str(amount)

    # Check if length is less than or equal to 10
    if len(amount_str) <= 10:
        # Format amount with asterisks as fill character and right alignment
        formatted_amount = f'{amount_str:*>10}'
    else:
        # If length is greater than 10, truncate to 10 characters
        formatted_amount = amount_str[:10]

    return formatted_amount


while True:
    dollar_amount_input = input("Enter the dollar amount: ")

    try:
        # Try to convert input to float
        dollar_amount = float(dollar_amount_input)
        # Format and print check-protected amount
        formatted_amount = format_check_protected_amount(dollar_amount)
        print("Check-protected amount:", formatted_amount)
        break  # Break out of the loop if successful
    except ValueError:
        print("Invalid input! Please enter a valid dollar amount.")
