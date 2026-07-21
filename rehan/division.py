print("=================================")
print("      Division Calculator")
print("=================================")

def divide_numbers(num1, num2):
    if num2 == 0:
        print("Error! Division by zero is not allowed.")
    else:
        result = num1 / num2
        print("----------------------------")
        print("First Number  :", num1)
        print("Second Number :", num2)
        print("Division      :", result)
        print("----------------------------")

choice = "yes"

while choice.lower() == "yes":

    print()
    print("Enter two numbers")

    first = float(input("Enter first number : "))
    second = float(input("Enter second number: "))

    divide_numbers(first, second)

    print()
    print("Menu")
    print("1. Continue")
    print("2. Exit")

    option = input("Enter your choice (yes/no): ")

    if option.lower() == "yes":
        choice = "yes"
    else:
        choice = "no"

print()
print("=================================")
print("Thank You for Using")
print("Division Calculator")
print("=================================")
print("Program Ended Successfully")
print("Have a Nice Day!")
print("Keep Practicing Python!")
print("Good Luck!")
print("===============================")