student_name1 = input("Enter name:")
roll_no = int(input("Roll no:"))

sub1 = float(input("ENTER SUB 1 MAKS"))
sub2 = float(input("ENTER SUB 2 MARKS"))
sub3 = float(input("ENTER SUB 3 MAKS"))
sub4 = float(input("ENTER SUB 4 MAKS"))
sub5 = float(input("ENTER SUB 5 MAKS"))

marks = sub1 + sub2 + sub3 + sub4 + sub5
prcntage = (marks / 500) * 100

if marks > 500 or marks < 0:
    result = "ERROR"
elif sub1 < 0 or sub2 < 0 or sub3 < 0 or sub4 < 0 or sub5 < 0 or sub1 > 100 or sub2 > 100 or sub3 > 100 or sub4 > 100 or sub5 > 100:
    result = "ERROR"
elif sub1 < 40 or sub2 < 40 or sub3 < 40 or sub4 < 40 or sub5 < 40:
    result = "Failed in subject"
elif prcntage < 40:
    result = "FAILED!!!!"

else:
    result = "******* PASSED *******"

if prcntage>=90:
        Grade = "O"
        Remark = "Outstanding"
elif prcntage>=80 and prcntage<=89:
        Grade = "A"
        Remark = "Excellent"
elif prcntage<=79 and prcntage>=70:
        Grade = "B"
        Remark= "Very Good"   
elif prcntage>=60 and prcntage<=69:
        Grade = "C"
        Remark = "Good"
elif prcntage<=59 and prcntage>=50:
        Grade = "D"
        Remark = "Needs Improvement" 
elif prcntage>=49 and prcntage<=40:
        Grade = "E"
        Remark ="Pass"
else :
        Grade = "F"
        Remark = "Fail"          


print(result)

print()
print("=======================================")
print("        SCHOOL RESULT PROCESSING       ")
print("=======================================")

print("Enter student name :", student_name1)
print("Enter roll number :", roll_no)

print("--- Enter Marks for 5 Subjects (0-100) ---")
print("Enter marks for Subject 1:", sub1)
print("Enter marks for Subject 2:", sub2)
print("Enter marks for Subject 3:", sub3)
print("Enter marks for Subject 4:", sub4)
print("Enter marks for Subject 5:", sub5)

print("=======================================")
print("          STUDENT REPORT CARD         ")
print("=======================================")

print(" Student Name  :", student_name1)
print("Roll Number    :", roll_no)

print("---------------------------------------")

print(f" Total Marks : {marks:.2f}/500")
print(f" Percentage  : {prcntage:.2f}%")
print(f" Result      : {result}")
print(f" Grade       : {Grade}")
print(f" Reamrks     : {Remark}")
print("=======================================")

