print("===================================")
print("   Multiplication Table Program")
print("===================================")

number = int(input("Enter a number: "))

print()
print("Multiplication Table of", number)
print("-----------------------------------")

for i in range(1, 11):
    result = number * i
    print(number, "x", i, "=", result)

print("-----------------------------------")
print("Table Completed Successfully")
print()

print("Squares from 1 to 10")
print("-----------------------------------")

for i in range(1, 11):
    square = i * i
    print("Square of", i, "=", square)

print("-----------------------------------")
print()

print("Even Numbers from 1 to 20")
print("-----------------------------------")

for i in range(1, 21):
    if i % 2 == 0:
        print(i)

print("-----------------------------------")
print()

print("Countdown")
print("-----------------------------------")

for i in range(5, 0, -1):
    print(i)

print("-----------------------------------")
print("Program Finished")
print("Thank You!")
print("Keep Practicing Python!")
print("Loops are very useful.")
print("Good Luck!")
print("===================================")
