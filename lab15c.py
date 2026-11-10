students = {
    101: {
        "Name": "Aman",
        "Branch": "BCA AI",
        "Sem": 2,
        "Marks": [85, 90, 78]
    },
    102: {
        "Name": "Riya",
        "Branch": "BCA AI",
        "Sem": 1,
        "Marks": [92, 88, 95]
    },
    104: {
        "Name": "Simran",
        "Branch": "BCA AI",
        "Sem": 1,
        "Marks": [88, 91, 84]
    }
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

    choice = int(input("Enter your choice (1-7): "))

    if choice == 1:
        print("--- Enrolled Student Records ---")
        for roll, student in students.items():
            print("Roll No:", roll,
                  "| Name:", student["Name"],
                  "| Branch:", student["Branch"],
                  "| Sem:", student["Sem"],
                  "| Marks:", student["Marks"])
        print("Total Enrolled Students:", len(students))
    elif choice == 2:
        roll = int(input("Enter Roll Number to search: "))
        if roll in students:
            student = students[roll]
            print("\nStudent Found")
            print("Roll No:", roll)
            print("Name:", student["Name"])
            print("Branch:", student["Branch"])
            print("Semester:", student["Sem"])
            print("Marks:", student["Marks"])
        else:
            print("Student not found.")
    elif choice == 3:
        roll = int(input("Enter Roll Number: "))
        if roll in students:
            print("Roll Number already exists.")
        else:
            name = input("Enter Student Name: ")
            branch = input("Enter Branch: ")
            sem = int(input("Enter Semester: "))
            marks = []
            print("Enter marks of 3 subjects:")
            for i in range(3):
                mark = int(input("Enter marks: "))
                marks.append(mark)
            students[roll] = {
                "Name": name,
                "Branch": branch,
                "Sem": sem,
                "Marks": marks
            }
            print("Student registered successfully.")
    elif choice == 4:
        roll = int(input("Enter Roll Number to update: "))
        if roll in students:
            print("1. Update Branch")
            print("2. Update Semester")
            option = int(input("Select field to update: "))
            if option == 1:
                new_branch = input("Enter new Branch: ")
                students[roll]["Branch"] = new_branch
                print("Branch updated successfully.")
            elif option == 2:
                new_sem = int(input("Enter new Semester: "))
                students[roll]["Sem"] = new_sem
                print("Semester updated successfully.")
            else:
                print("Invalid option.")
        else:
            print("Student not found.")
    elif choice == 5:
        roll = int(input("Enter Roll Number for Academic Performance: "))
        if roll in students:
            student = students[roll]
            total = sum(student["Marks"])
            average = total / len(student["Marks"])
            print("================ ACADEMIC REPORT ================")
            print("Student Name:", student["Name"], "(Roll:", roll, ")")
            print("Subject Marks:", student["Marks"])
            print("Total Marks:", total, "/", len(student["Marks"]) * 100)
            print("Average Marks:", average, "%")
            if average >= 40:
                print("Final Result: PASS")
            else:
                print("Final Result: FAIL")
            print("==================================================")
        else:
            print("Student not found.")
    elif choice == 6:
        roll = int(input("Enter Roll Number to delete: "))
        student = students.get(roll)
        if student is not None:
            students.pop(roll, None)
            print("[SUCCESS] Record for", student["Name"],
                  "(Roll No:", roll, ") deleted successfully.")
        else:
            print("Student not found.")
    elif choice == 7:
        print("Thank you for using Student Information System.")
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 7.")