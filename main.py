def add_student():
    with open("students.txt", "a") as file:
        student_id = input("Enter Student ID: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        course = input("Enter Course: ")

        file.write(f"{student_id},{name},{age},{course}\n")
        print("Student added successfully")


def view_students():
    with open("students.txt", "r") as file:
        students = file.readlines()
        if not students:
            print("No students found")
        else:
            print("\nID, Name, Age, Course")
            print("-" * 30)
            for student in students:
                print(student.strip())


def search_student():
    search_id = input("Enter Student ID to search: ")
    found = False

    with open("students.txt", "r") as file:
        for student in file:
            data = student.strip().split(",")
            if data[0] == search_id:
                print("\nStudent Found")
                print("ID:", data[0])
                print("Name:", data[1])
                print("Age:", data[2])
                print("Course:", data[3])
                found = True
                break

    if not found:
        print("Student not found")


def delete_student():
    student_id = input("Enter Student ID to delete: ")
    students = []

    with open("students.txt", "r") as file:
        students = file.readlines()

    with open("students.txt", "w") as file:
        deleted = False
        for student in students:
            if not student.startswith(student_id + ","):
                file.write(student)
            else:
                deleted = True

    if deleted:
        print("Student deleted successfully")
    else:
        print("Student ID not found")


while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        delete_student()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice")
