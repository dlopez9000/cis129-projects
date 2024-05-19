# Final Lab 13
# Darlene Lopez
# 5/18/2024
# This is a pseduocode using Python to brainstorm a program to help check in patients at a veterinary clinic faster and have a more simple UI for employees.

# Define a class for PetPatient
Class PetPatient:
    # Initialize the class with name, species, breed, age, owner_name, visit_date, and visit_reason
    Method __init__(self, name, species, breed, age, owner_name, visit_date, visit_reason):
        Set self.name = name
        Set self.species = species
        Set self.breed = breed
        Set self.age = age
        Set self.owner_name = owner_name
        Set self.visit_date = visit_date
        Set self.visit_reason = visit_reason

    # Method to represent the PetPatient object as a string
    Method __str__(self):
        Return formatted string with pet's details

# Define a class for VetLog to manage patient records
Class VetLog:
    # Initialize the class with an empty list for patients
    Method __init__(self):
        Set self.patients = []

    # Method to add a new patient
    Method add_patient(self, patient):
        Append patient to self.patients

    # Method to display all patients
    Method display_patients(self):
        If self.patients is empty:
            Print "No patient records found."
        Else:
            For each patient in self.patients:
                Print patient

    # Method to search for a patient by name
    Method search_patient(self, name):
        For each patient in self.patients:
            If patient.name equals name:
                Print patient
                Return
        Print "Patient not found."

# Main function to run the program
Function main():
    Create an instance of VetLog called vet_log

    While True:
        Print menu options
        Input choice from user

        If choice is "1":
            Input pet details (name, species, breed, age, owner_name, visit_date, visit_reason)
            Create an instance of PetPatient with the provided details
            Call vet_log.add_patient() with the new patient

        Else if choice is "2":
            Call vet_log.display_patients()

        Else if choice is "3":
            Input name to search
            Call vet_log.search_patient() with the name

        Else if choice is "4":
            Print "Exiting the program."
            Break

        Else:
            Print "Invalid choice. Please try again."

# Run the main function if the script is executed
If __name__ == "__main__":
    Call main()
