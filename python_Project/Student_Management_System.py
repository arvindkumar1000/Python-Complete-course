# Student Management System using Loop, OOP, and Functions

class Student:
    def __init__(self, student_id, name, marks):
        self.student_id = student_id
        self.name = name
        self.marks = marks

    def display(self):
        print(f"ID: {self.student_id}, Name: {self.name}, Marks: {self.marks}")


class StudentManagement:
    def __init__(self):
        self.students = []

    def add_student(self):
        student_id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        marks = float(input("Enter Marks: "))

        student = Student(student_id, name, marks)
        self.students.append(student)
        print("✅ Student added successfully!\n")

    def view_students(self):
        if not self.students:
            print("⚠️ No students found.\n")
        else:
            print("\n📋 Student List:")
            for student in self.students:   
                student.display()
            print()

    def search_student(self):
        search_id = input("Enter Student ID to search: ")
        for student in self.students:       
            if student.student_id == search_id:
                print("🎯 Student Found:")
                student.display()
                return
        print("❌ Student not found.\n")
    def delete_student(self):
        delete_id = input("Enter student Id to delete: ")
        for student in self.students:
            if student.student_id == delete_id:
                print("🗑️ Delete student record !")
                return


def main():
    system = StudentManagement()

    while True:  
        print("===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete student")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            system.add_student()       
        elif choice == "2":
            system.view_students()
        elif choice == "3":
            system.search_student()
        elif choice == "4":
            system.delete_student()
        elif choice == "5":
            print("👋 Exiting program. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Try again.\n")


# Program starts here
main()
