# Lab 11: 9.2
# Darlene Lopez
# 4/15/2024
# This program helps to save grades to grades.txt
def main():
    # Open the file in write mode
    with open("grades.txt", "w") as file:
        # Prompt the user for grades until they input the sentinel value
        print("Enter grades (enter 'q' to quit):")
        while True:
            grade = input("Grade: ")
            if grade.lower() == 'q':
                break
            file.write(grade + "\n")

    print("Grades have been saved to grades.txt")


if __name__ == "__main__":
    main()
# Open the grades.txt file for reading
with open('grades.txt', 'r') as file:
    # Read all lines from the file
    lines = file.readlines()

# Convert grades from strings to floats
grades = [float(line.strip()) for line in lines]

# Display individual grades
print("Individual Grades:")
for grade in grades:
    print(grade)

# Calculate total, count, and average
total = sum(grades)
count = len(grades)
average = total / count

# Display total, count, and average
print("\nTotal:", total)
print("Count:", count)
print("Average:", average)
