# Python Multiplication Program

def multiply(a, b):
    return a * b

print("Welcome to Multiplication Program")
print("---------------------------------")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = multiply(num1, num2)

print("Multiplication Result =", result)

print("\nExamples")

print("2 x 3 =", multiply(2, 3))
print("4 x 5 =", multiply(4, 5))
print("6 x 7 =", multiply(6, 7))
print("8 x 9 =", multiply(8, 9))
print("10 x 11 =", multiply(10, 11))

print("\nMultiplication Table")

table_num = int(input("Enter a number for table: "))

for i in range(1, 11):
    print(table_num, "x", i, "=", multiply(table_num, i))

print("\nList Multiplication")

numbers = [1, 2, 3, 4, 5]

for n in numbers:
    print(n, "x 10 =", multiply(n, 10))

print("\nNested Loop Example")

for i in range(1, 4):
    for j in range(1, 4):
        print(i, "x", j, "=", multiply(i, j))

print("\nLarge Number Example")

a = 100
b = 200

print(a, "x", b, "=", multiply(a, b))

print("\nProgram Finished")
print("Thank You")
print("Keep Practicing Python")
print("Learn Functions")
print("Learn Loops")
print("Learn Lists")
print("Learn Git and GitHub")
print("Become a Python Developer")
print("Happy Coding!")
