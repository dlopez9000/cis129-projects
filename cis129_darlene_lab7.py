# Module 7 lab
# Darlene Lopez
# 3/10/2024
# This program calculates theater seating tickets

# Constant
SECTIONS = ['A', 'B', 'C']
SEAT_PRICES = {'A': 20, 'B': 15, 'C': 10}
SEAT_COUNTS = {'A': 300, 'B': 500, 'C': 200}


# Function to display welcome message and seating options
def display_welcome():
    print("Welcome to Selkie Theater!")
    print("*ੈ✩‧₊˚༺☆༻*ੈ✩‧₊˚")
    print("Section seating capacities:")
    for section in SECTIONS:
        print(f"Section {section}: {SEAT_COUNTS[section]} seats, ${SEAT_PRICES[section]} each")
    print()


# Function to validate input for the seats and tickets
def validate_input(section, num_tickets):
    if section not in SECTIONS:
        return False
    if not num_tickets.isdigit():
        return False
    if int(num_tickets) > SEAT_COUNTS[section]:
        return False
    return True


# Function to calculate subtotal for tickets sold
def calculate_subtotal(sales):
    subtotal = 0
    for section, tickets_sold in sales.items():
        subtotal += tickets_sold * SEAT_PRICES[section]
    return subtotal


# Main function of the program
def main():
    display_welcome()
    total_sales = {}
    while True:
        section = input("Enter section (A, B, C) or 'done' to finish: ").upper()
        if section == 'DONE':
            break
        if section not in SECTIONS:
            print("Invalid section. Please enter A, B, or C.")
            continue
        num_tickets = input(f"Enter number of tickets for section {section}: ")
        if not validate_input(section, num_tickets):
            print("Invalid input. Please enter a valid number of tickets.")
            continue
        num_tickets = int(num_tickets)
        if section not in total_sales:
            total_sales[section] = 0
        total_sales[section] += num_tickets
        subtotal = calculate_subtotal(total_sales)
        print(f"Subtotal: ${subtotal}")
    overall_total = calculate_subtotal(total_sales)
    print("\nOverall total income:", overall_total)
    print("Number of seats and subtotals for each section:")
    for section in SECTIONS:
        print(
            f"Section {section}: {total_sales.get(section, 0)} seats, ${total_sales.get(section, 0) * SEAT_PRICES[section]}")


if __name__ == "__main__":
    main()
