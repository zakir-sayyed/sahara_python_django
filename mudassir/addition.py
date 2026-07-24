# Python Addition Program
addition the multipale number 
def add(a, b)
    return a + b

print("Welcome to Addition Program")
print("---------------------------")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = add(num1, num2)
 
print("Addition Result =", result)

print("\nExamples")

print("10 + 20 =", add(10, 20))
print("30 + 40 =", add(30, 40))
print("50 + 60 =", add(50, 60))
print("70 + 80 =", add(70, 80))
print("90 + 100 =", add(90, 100))

print("\nAddition Table")

table_num = int(input("Enter a number: "))

for i in range(1, 11):
    print(table_num, "+", i, "=", add(table_num, i))

print("\nList Addition")

numbers = [10, 20, 30, 40, 50]

for n in numbers:
    print(n, "+ 100 =", add(n, 100))

print("\nNested Loop Example")

for i in range(1, 4):
    for j in range(1, 4):
        print(i, "+", j, "=", add(i, j))

print("\nLarge Number Example")

a = 1000
b = 2000

print(a, "+", b, "=", add(a, b))

print("\nProgram Finished")
print("Thank You")
print("Keep Practicing Python")
print("Learn Functions")
print("Learn Loops")
print("Learn Lists")
print("Learn Git and GitHub")
print("Become a Python Developer")
print("Happy Coding!")
