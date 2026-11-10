students = {
    "101": {
        "Name": "Aman",
        "Branch": "BCA AI",
        "Semester": "1",
        "Marks": [85, 90, 78]
    },
    "102": {
        "Name": "Riya",
        "Branch": "BCA AI",
        "Semester": "1",
        "Marks": [92, 88, 95]
    },
    "103": {
        "Name": "Karan",
        "Branch": "BCA AI",
        "Semester": "1",
        "Marks": [74, 88, 82]
    }
}
while True:
    print("\n" + "="*50)
    print("      STUDENT INFORMATION MANAGEMENT SYSTEM      ")
    print("="*50)
    print("Select an operation:")
    print("1. View All Students")
    print("2. Search Student by Roll Number")
    print("3. Register New Student")
    print("4. Update Student Details")
    print("5. View Academic Performance")
    print("6. Delete Student Record")
    print("7. Exit")
    
    choice = input("\nEnter your choice (1-7): ").strip()
    if choice == '1':
        print("--- Enrolled Student Records ---")
        if not students:
            print("No student records found.")
        else:
            for roll_no, details in students.items():
                print(f"Roll No: {roll_no}  | Name: {details['Name']}  | Branch: {details['Branch']}  | Sem: {details['Semester']}  | Marks: {details['Marks']}")
            print(f"Total Enrolled Students: {len(students)}")
    elif choice == '2':
        roll_no = input("Enter Roll Number to search: ").strip()
        record = students.get(roll_no)
        if record:
            print(f"[FOUND] Record for Roll No {roll_no}:")
            print(f"  Name     : {record['Name']}")
            print(f"  Branch   : {record['Branch']}")
            print(f"  Semester : {record['Semester']}")
            print(f"  Marks    : {record['Marks']}")
        else:
            print(f"[ERROR] Student with Roll Number {roll_no} not found.")
    elif choice == '3':
        print("--- Register New Student ---")
        roll_no = input("Enter Roll Number: ").strip()
        if roll_no in students:
            print(f"[ERROR] Student with Roll Number {roll_no} already exists.")
        else:
            name = input("Enter Student Name: ").strip()
            branch = input("Enter Branch (e.g. BCA AI): ").strip()
            semester = input("Enter Semester: ").strip()
            
            print("Enter marks obtained in 3 subjects:")
            marks = []
            for i in range(1, 4):
                mark = int(input(f"  Subject {i}: "))
                marks.append(mark)
                
            students[roll_no] = {
                "Name": name,
                "Branch": branch,
                "Semester": semester,
                "Marks": marks
            }
            print(f"\n[SUCCESS] Student '{name}' (Roll No: {roll_no}) registered successfully.")
    elif choice == '4':
        print("--- Update Student Details ---")
        roll_no = input("Enter Roll Number to update: ").strip()
        if roll_no in students:
            print(f"Updating details for {students[roll_no]['Name']}:")
            branch = input("Enter new Branch (leave blank to keep unchanged): ").strip()
            semester = input("Enter new Semester (leave blank to keep unchanged): ").strip()
            
            if branch:
                students[roll_no]['Branch'] = branch
            if semester:
                students[roll_no]['Semester'] = semester
                
            print(f"[SUCCESS] Student details updated successfully.")
        else:
            print(f"[ERROR] Student with Roll Number {roll_no} not found.")
    elif choice == '5':
        print("--- View Academic Performance ---")
        roll_no = input("Enter Roll Number: ").strip()
        record = students.get(roll_no)
        if record:
            total = sum(record['Marks'])
            percentage = total / len(record['Marks'])
            status = "Pass" if percentage >= 40 else "Fail"
            
            print(f"Academic Report for {record['Name']} (Roll No: {roll_no}):")
            print(f"  Total Marks : {total} / 300")
            print(f"  Percentage  : {percentage:.2f}%")
            print(f"  Result      : {status}")
        else:
            print(f"[ERROR] Student with Roll Number {roll_no} not found.")
    elif choice == '6':
        print("--- Delete Student Record ---")
        roll_no = input("Enter Roll Number to delete: ").strip()
        removed_student = students.pop(roll_no, None)
        if removed_student:
            print(f"[SUCCESS] Record for Roll No {roll_no} ({removed_student['Name']}) deleted successfully.")
        else:
            print(f"[ERROR] Student with Roll Number {roll_no} not found.")
    elif choice == '7':
        print("\nExiting the system. Goodbye!")
        break
    else:
        print("[ERROR] Invalid choice. Please enter a number between 1 and 7.")