"""
1.  Takes two numbers as input from the user.
2.  Performs the basic mathematical operations on these two numbers:
    Addition, Subtraction, Multiplication, Division
3.  Displays the results of each operation on the screen.
"""
# Accept the numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculations
Addition = num1 + num2
Substraction = num1 - num2
Multiplication = num1 * num2
Division = num1 / num2

# Show result
print(" ")
print('Addition: ', Addition)
print('Substraction: ', Substraction)
print('Multiplication: ', Multiplication)
print('Division: ', round(Division,2))

