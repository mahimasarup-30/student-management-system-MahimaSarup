from student import Student

students = []


def find(roll):
    for student in students:
        if student.roll == roll:
            return student
        else:
            return None

#       1. Add Student
def add_student():
    roll= int(input("Enter Roll Number: "))
    name = input("Enter Name: ")
    marks = float(input("Enter Marks: "))

    student = Student(roll, name, marks)
    students.append(student)
    print("Student Added Successfully.")




#   2. View Students
def view_Students():
    if len(students)==0:
        print("No student found!")

    for student in students:
        student.display()


#   3. Search Student
def search_student():
    roll = int(input("Enter Roll Number: "))
    student = find(roll)

    if student:
        student.display()
    else:
        print("Student Not Found")


#   4. Update Marks
def update_marks():
    roll = int(input("Enter Roll Number: "))
    student = find(roll)

    if student:
        marks = float(input("Enter New Marks: "))

        if marks < 0 or marks > 100:
            print("Marks should be between 0 and 100.")
            return

        student.update_marks(marks)
        print("Marks Updated Successfully")


#   5. Delete Student
def delete_student():
    roll = int(input("Enter Roll Number: "))

    student = find(roll)

    if student:
        students.remove(student)
        Student.total_students =Student.get_total_students-1
        print("Student Deleted Successfully")
    else:
        print("Student Not Found")


#       6. Show Topper
def show_topper():
    topper = students[0]

    for student in students:
        if student.marks > topper.marks:
            topper = student

            print("\nTopper Details")
            topper.display()

def menu():
    while True:
        print("\n==============================")
        print(" Student Management System")
        print("==============================")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Marks")
        print("5. Delete Student")
        print("6. Show Topper")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_Students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_marks()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            show_topper()

        elif choice == "7":
            print("Thank you!")
            break

        else:
            print("Invalid Choice!")


if __name__ == "__main__":
    menu()

