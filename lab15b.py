
students = {
    101: {
        "Name": "Aman",
        "Branch": "BCA AI",
        "Semester": 1,
        "Marks": [85, 90, 78],
    },
    102: {
        "Name": "Riya",
        "Branch": "BCA AI",
        "Semester": 1,
        "Marks": [92, 88, 95],
    },
    103: {
        "Name": "Karan",
        "Branch": "BCA AI",
        "Semester": 1,
        "Marks": [60, 55, 70],
    },
}

while True:
    print("Select an operation:")
    print("1. View All Students")
    print("2. Search Student by Roll Number")
    print("3. Register New Student")
    print("4. Update Student Details")
    print("5. View Academic Performance")
    print("6. Delete Student Record")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        if not students:
            print("[INFO] No student records available.")
        else:
            print("--- Enrolled Student Records ---")
            for roll, details in students.items():
                print(
                    f"Roll No: {roll} | Name: {details['Name']} | Branch: {details['Branch']} | "
                    f"Sem: {details['Semester']} | Marks: {details['Marks']}"
                )
            print(f"Total Students: {len(students)}")
    elif choice == "2":
        try:
            roll = int(input("Enter Roll Number to search: "))
            student = students.get(roll)
            if student:
                print(f"[FOUND] Record for Roll No {roll}:")
                print(f"Name: {student['Name']}")
                print(f"Branch: {student['Branch']}")
                print(f"Semester: {student['Semester']}")
                print(f"Marks: {student['Marks']}")
            else:
                print(f"[ERROR] Student with Roll Number {roll} not found.")
        except ValueError:
            print("[ERROR] Invalid input. Roll Number must be an integer.")
    elif choice == "3":
        try:
            roll = int(input("Enter Roll Number: "))
            if roll in students:
                print(
                    f"[ERROR] Roll Number {roll} already exists! Please use a unique Roll Number."
                )
            else:
                name = input("Enter Name: ")
                branch = input("Enter Branch: ")
                semester = int(input("Enter Semester: "))
                print("Enter 3 subject marks:")
                m1 = float(input("  Subject 1: "))
                m2 = float(input("  Subject 2: "))
                m3 = float(input("  Subject 3: "))

                students[roll] = {
                    "Name": name,
                    "Branch": branch,
                    "Semester": semester,
                    "Marks": [m1, m2, m3],
                }
                print(
                    f"[SUCCESS] Student '{name}' (Roll No: {roll}) registered successfully."
                )
        except ValueError:
            print("[ERROR] Invalid numerical input entered.")
    elif choice == "4":
        try:
            roll = int(input("Enter Roll Number to update: "))
            if roll in students:
                student = students[roll]
                print(
                    f"Current details for {student['Name']} (Roll {roll}):"
                )
                print(f"1. Branch: {student['Branch']} | 2. Semester: {student['Semester']}")
                field_choice = input(
                    "Choose field to update (1 for Branch, 2 for Semester): "
                )
                if field_choice == "1":
                    new_branch = input("Enter new branch: ")
                    student["Branch"] = new_branch
                    print(f"[SUCCESS] Branch updated to '{new_branch}'.")
                elif field_choice == "2":
                    new_sem = int(input("Enter new semester: "))
                    student["Semester"] = new_sem
                    print(f"[SUCCESS] Semester updated to '{new_sem}'.")
                else:
                    print("[ERROR] Invalid field selection choice.")
            else:
                print(f"[ERROR] Student with Roll Number {roll} not found.")
        except ValueError:
            print("[ERROR] Invalid numerical input entered.")
    elif choice == "5":
        try:
            roll = int(input("Enter Roll Number for Academic Performance: "))
            student = students.get(roll)
            if student:
                marks = student["Marks"]
                total = sum(marks)
                average = total / len(marks)
                result = "PASS" if average >= 40 else "FAIL"

                print("================ ACADEMIC REPORT ================")
                print(f"Student Name: {student['Name']} (Roll: {roll})")
                print(f"Subject Marks: {marks}")
                print(f"Total Marks: {total:.0f} / {len(marks)*100}")
                print(f"Average Marks: {average:.2f}%")
                print(f"Final Result : {result}")
                print("=================================================")
            else:
                print(f"[ERROR] Student with Roll Number {roll} not found.")
        except ValueError:
            print("[ERROR] Invalid input. Roll Number must be an integer.")
    elif choice == "6":
        try:
            roll = int(input("Enter Roll Number to delete: "))
            removed_student = students.pop(roll, None)
            if removed_student:
                print(
                    f"[SUCCESS] Record for '{removed_student['Name']}' (Roll No: {roll}) deleted successfully."
                )
            else:
                print(f"[ERROR] Student with Roll Number {roll} not found.")
        except ValueError:
            print("[ERROR] Invalid input. Roll Number must be an integer.")

    elif choice == "7":
        print("Thank you for using the Student Info Management System. Goodbye!")
        break
    else:
        print("[ERROR] Invalid choice! Please select a valid option between 1 and 7.")