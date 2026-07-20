# Beginner Python Program

print("=== Student Report Card ===")

# Taking input
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Marks
math = int(input("Enter Math marks: "))
science = int(input("Enter Science marks: "))
english = int(input("Enter English marks: "))

# Total and Average
total = math + science + english
average = total / 3

print("\n----- Report -----")
print("Name:", name)
print("Age:", age)
print("Total Marks:", total)
print("Average:", average)

# Grade
if average >= 90:
    grade = "A+"
elif average >= 75:
    grade = "A"
elif average >= 60:
    grade = "B"
elif average >= 40:
    grade = "C"
else:
    grade = "Fail"

print("Grade:", grade)

# Subject list
subjects = ["Math", "Science", "English"]
print("\nSubjects:")
for subject in subjects:
    print(subject)

# Function
def welcome(student):
    print("\nWelcome,", student)
    print("Keep learning Python!")

welcome(name)

print("\nNumbers from 1 to 5:")
for i in range(1, 6):
    print(i)

print("\nProgram Completed Successfully!")
