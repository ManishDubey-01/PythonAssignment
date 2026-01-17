'''
Task 2: Write and Append Data to a File

Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.
'''

# open in write mode and write first conent
fh = open("output.txt", "wt")
content = input("Enter text to write to the file: ")
fh.write(content + "\n")
fh.close()
print("Data successfully written to output.txt\n")

# open in append mode and write additional contents
fh = open("output.txt", "at")
content = input("Enter additional text to append: ")
fh.write(content + "\n")
fh.close()
print("Data successfully appended to output.txt\n")

# read the content of the file
fh = open("output.txt", "rt")
print("Final content of output.txt")
for line in fh:
    print(line.rstrip('\n'))
fh.close()
