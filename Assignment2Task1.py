'''
Task 1: Check if a Number is Even or Odd
Problem Statement:  Write a Python program that:
1. 	Takes an integer input from the user.
2. 	Checks whether the number is even or odd using an if-else statement.
3. 	Displays the result accordingly.
'''

# take a number as input
num = int(input("Enter a number: "))
numtype = "odd"

# check if number is divisible by 2
if num % 2 == 0:
    numtype = "even"
else:
    numtype = "odd"

# print result
print(f"{num} is an {numtype} number")