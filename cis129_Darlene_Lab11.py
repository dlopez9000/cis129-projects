# Lab 11: 9.1
# Darlene Lopez
# 4/13/2024
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
