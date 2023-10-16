# A class to represent a student with ID, name, and age.
class Student:
    def __init__(self, ID, name, age):
        self.ID = ID
        self.name = name
        self.age = age

# Initialize the Student Management System with an empty list of students.
class StudentManagementSystem:
    def __init__(self):
        self.students = []
        
    # Accepts student information from the user and creates a Student object.
    def accept_student(self):
        ID = int(input("Enter ID Number: "))
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))

    # Display a list of all students and their details.
    def display_students(self):
        print("Student List:")
        for student in self.students:
            print(f"ID: {student.ID}, Name: {student.name}, Age: {student.age}")

    # Search for a student by their ID and display their details if found.
    def search_student(self, ID):
        for student in this.students:
            if student.ID == ID:
                print(f"Student found - ID: {student.ID}, Name: {student.name}, Age: {student.age}")
                return
        print("Student not found!")

    # Delete a student from the list based on their ID.
    def delete_student(self, ID):
        for student in self.students:
            if student.ID == ID:
                self.students.remove(student)
                print("Student deleted successfully!")
                return
        print("Student not found!")

    # Update a student's information based on their ID.
    def update_student(self, ID):
        for student in self.students:
            if student.ID == ID:
                name = input("Enter updated name: ")
                age = int(input("Enter updated age: "))
                student.name = name
                student.age = age
                print("Student information updated successfully!")
                return
        print("Student not found!")

if __name__ == "__main__":
    sms = StudentManagementSystem()

    # Display a menu for the user and take their choice.
    while True:
        print("\nStudent Management System")
        print("1. Accept Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Update Student")
        print("6. Exit")
              
        # Process the user's choice and execute the corresponding function.
        choice = int(input("Enter your choice: "))

        if choice == 1:
            sms.accept_student()
        elif choice == 2:
            sms.display_students()
        elif choice == 3:
            ID = int(input("Enter ID Number to search: "))
            sms.search_student(ID)
        elif choice == 4:
            ID = int(input("Enter ID Number to delete: "))
            sms.delete_student(ID)
        elif choice == 5:
            ID = int(input("Enter ID Number to update: "))
            sms.update_student(ID)
        elif choice == 6:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
