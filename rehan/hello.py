print("===== Student Result =====")

name = input("Enter student name: ")
marks = int(input("Enter marks (0-100): "))

if marks >= 90:
    grade = "A+"
    print("Excellent!")
elif marks >= 80:
    grade = "A"
    print("Very Good!")
elif marks >= 70:
    grade = "B"
    print("Good!")
elif marks >= 60:
    grade = "C"
    print("Average!")
elif marks >= 35:
    grade = "D"
    print("Pass")
else:
    grade = "F"
    print("Fail")

print("----------------------")
print("Student Name :", name)
print("Marks        :", marks)
print("Grade        :", grade)
print("----------------------")
print("Result Generated Successfully")
print("Thank You!")
