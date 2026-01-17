'''
Task 1: Read a File and Handle Errors
Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.
'''

try:
    print("Reading the file content:")
    line_no = 1
    with open("sample.txt", "rt") as fh:
        for line in fh:
            print(f"Line{line_no}: {line.rstrip('\n')}")
    fh.close()
except FileNotFoundError:
    print("Error: The file sample.txt was not found")
