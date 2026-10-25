#Mini Project (W2): Student Management System
#Objective: Create a Python program to manage student records using a CSV file. 
#The system will allow you to add, delete, and search for students, and save changes permanently to a file.


import csv
import os

FILE = "students.csv"

# Create CSV file if it does not exist
if not os.path.exists(FILE):
    with open(FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Roll Number", "Name", "Marks"])


# Add student
def add_student():
    roll = input("Enter roll number: ")

    students = read_students()

    for student in students:
        if student["Roll Number"] == roll:
            print("Roll number already exists!")
            return

    name = input("Enter student name: ")
    marks = input("Enter marks: ")

    try:
        marks_value = float(marks)
        if not 0 <= marks_value <= 100:
            print("Marks must be between 0 and 100.")
            return
    except ValueError:
        print("Please enter valid numeric marks.")
        return

    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([roll, name, marks_value])

    print("Student added successfully!")


# Read all students
def read_students():
    with open(FILE, "r", newline="") as f:
        return list(csv.DictReader(f))


# Search student
def search_student():
    roll = input("Enter roll number to search: ")
    students = read_students()

    for student in students:
        if student["Roll Number"] == roll:
            print("\nStudent Found")
            print("Roll Number:", student["Roll Number"])
            print("Name:", student["Name"])
            print("Marks:", student["Marks"])
            return

    print("Student not found!")


# Delete student
def delete_student():
    roll = input("Enter roll number to delete: ")
    students = read_students()

    updated_students = [
        student for student in students
        if student["Roll Number"] != roll
    ]

    if len(updated_students) == len(students):
        print("Student not found!")
        return

    with open(FILE, "w", newline="") as f:
        fields = ["Roll Number", "Name", "Marks"]
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(updated_students)

    print("Student deleted successfully!")


# Display all students
def display_students():
    students = read_students()

    if not students:
        print("No student records found.")
        return

    print("\n--- Student Records ---")
    for student in students:
        print(
            "Roll:", student["Roll Number"],
            "| Name:", student["Name"],
            "| Marks:", student["Marks"]
        )


# Main menu
while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Delete Student")
    print("4. Display All Students")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        search_student()
    elif choice == "3":
        delete_student()
    elif choice == "4":
        display_students()
    elif choice == "5":
        print("Data saved. Exiting program.")
        break
    else:
        print("Invalid choice! Please try again.")
