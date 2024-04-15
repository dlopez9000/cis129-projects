# Lab 11: 9.3
# Darlene Lopez
# 4/15/2024
# This program stores student exam scores
import csv
def main():
    # Open the grades.csv file in write mode
    with open("grades.csv", "w", newline='') as csvfile:
        # Create a CSV writer object
        writer = csv.writer(csvfile)

        # header row
        writer.writerow(['firstname', 'lastname', 'exam1grade', 'exam2grade', 'exam3grade'])

        # Prompt the instructor to enter student records
        while True:
            # Prompt for student information
            first_name = input("Enter student's first name (or 'q' to quit): ")
            if first_name.lower() == 'q':
                break
            last_name = input("Enter student's last name: ")
            exam1 = int(input("Enter student's exam 1 grade: "))
            exam2 = int(input("Enter student's exam 2 grade: "))
            exam3 = int(input("Enter student's exam 3 grade: "))

            # Write the student record to the CSV file
            writer.writerow([first_name, last_name, exam1, exam2, exam3])

    print("Student records have been saved to grades.csv")

if __name__ == "__main__":
    main()
