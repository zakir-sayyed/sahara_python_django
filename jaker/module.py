# mymodule.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Division by zero not allowed"
    return a / b

print("Welcome to Python Module Program")
print("--------------------------------")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Addition =", add(num1, num2))
print("Subtraction =", subtract(num1, num2))
print("Multiplication =", multiply(num1, num2))
print("Division =", divide(num1, num2))

print("\nExamples")

print("10 + 5 =", add(10, 5))
print("10 - 5 =", subtract(10, 5))
print("10 * 5 =", multiply(10, 5))
print("10 / 5 =", divide(10, 5))

print("\nLoop Example")

for i in range(1, 6):
    print(i, "+", i, "=", add(i, i))

print("\nList Example")

numbers = [10, 20, 30, 40, 50]

for n in numbers:
    print(n, "* 2 =", multiply(n, 2))

print("\nProgram Completed")
print("Module Functions Used")
print("add()")
print("subtract()")
print("multiply()")
print("divide()")
print("Learn Python Modules")
print("Practice Daily")
print("Keep Coding")
print("Become a Python Developer")
print("Thank You")
