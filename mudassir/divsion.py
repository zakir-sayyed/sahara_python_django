# Python Division Program

def divide(a, b):
    if b == 0:
        return "Division by zero is not allowed"
    return a / b

print("Welcome to Division Program")
print("---------------------------")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = divide(num1, num2)

print("Division Result =", result)

print("\nExamples")

print("10 / 2 =", divide(10, 2))
print("20 / 4 =", divide(20, 4))
print("30 / 5 =", divide(30, 5))
print("40 / 8 =", divide(40, 8))
print("50 / 10 =", divide(50, 10))

print("\nDivision Table")

table_num = int(input("Enter a number: "))

for i in range(1, 11):
    print(table_num, "/", i, "=", divide(table_num, i))

print("\nList Division")

numbers = [100, 200, 300, 400, 500]

for n in numbers:
    print(n, "/ 10 =", divide(n, 10))

print("\nNested Loop Example")

for i in range(1, 4):
    for j in range(1, 4):
        print(i * 10, "/", j, "=", divide(i * 10, j))

print("\nLarge Number Example")

a = 1000
b = 20

print(a, "/", b, "=", divide(a, b))

print("\nProgram Finished")
print("Thank You")
print("Keep Practicing Python")
print("Learn Functions")
print("Learn Loops")
print("Learn Lists")
print("Learn Git and GitHub")
print("Become a Python Developer")
print("Happy Coding!")
