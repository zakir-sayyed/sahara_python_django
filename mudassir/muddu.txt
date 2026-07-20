# Python Subtraction Program

def subtract(a, b):
    return a - b

print("Welcome to Subtraction Program")
print("-----------------------------")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = subtract(num1, num2)

print("Result =", result)

print("\nMore Examples")
print("10 - 5 =", subtract(10, 5))
print("20 - 8 =", subtract(20, 8))
print("30 - 15 =", subtract(30, 15))
print("40 - 25 =", subtract(40, 25))
print("50 - 35 =", subtract(50, 35))

print("\nLoop Example")

for i in range(1, 6):
    a = i * 10
    b = i
    print(a, "-", b, "=", subtract(a, b))

print("\nList Example")

numbers = [100, 90, 80, 70, 60]

for i in range(len(numbers) - 1):
    print(
        numbers[i],
        "-",
        numbers[i + 1],
        "=",
        subtract(numbers[i], numbers[i + 1])
    )

print("\nNegative Number Example")

x = 25
y = 50

print(x, "-", y, "=", subtract(x, y))

print("\nProgram Completed")

print("Thank You")
print("Learn Python Daily")
print("Practice More")
print("Keep Coding")
print("Success Ahead")
