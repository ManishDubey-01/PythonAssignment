'''
Task 1: Calculate Factorial Using a Function

Problem Statement: Write a Python program that:
1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
2.   Returns the calculated factorial.
3.   Calls the function with a sample number and prints the output.
'''

def factorial(number):
    if number <= 1:
        return 1
    else:
        return number * factorial(number - 1)

num1 = int(input("Enter a number: "))
print(f"Factorial of {num1} is : {factorial(num1)}")