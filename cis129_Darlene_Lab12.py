# Lab 12
# Darlene Lopez
# 4/27/2024
# This program is for using pet classes and to store pet information.
class Pet:
    # Constructor
    def __init__(self, n, t, a):
        # Fields
        self.name = n
        self.type = t
        self.age = a

    # Mutators
    def set_name(self, n):
        self.name = n

    def set_type(self, t):
        self.type = t

    def set_age(self, a):
        self.age = a

    # Accessors
    def get_name(self):
        return self.name

    def get_type(self):
        return self.type

    def get_age(self):
        return self.age


# Main function
def main():
    # Create a Pet object
    animal = Pet("", "", 0)

    # Get values for a pet
    input_name = input("Enter your pet's name: ")
    animal.set_name(input_name)
    print()  # Empty print statement for spacing

    input_type = input("Enter your pet's type: ")
    animal.set_type(input_type)
    print()  # Empty print statement for spacing

    while True:
        try:
            input_age = int(input("Enter your pet's age: "))
            if input_age < 0:
                raise ValueError("Age cannot be negative.")
            animal.set_age(input_age)
            break
        except ValueError as e:
            print("Error:", e)
            print("Please enter a valid age.")
    print()  # Empty print statement for spacing

    # Show values for this pet
    print("Your pet's name :", animal.get_name())
    print("Your pet's type :", animal.get_type())
    print("Your pet's age :", animal.get_age())


if __name__ == "__main__":
    main()
