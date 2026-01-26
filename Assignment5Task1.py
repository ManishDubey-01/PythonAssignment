'''
Task 1: Create a Dictionary of Student Marks

Problem Statement: Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.
'''
# Dictionary of student's marks
student_data = {"Alice" : 40, "John" : 50, "Marry": 66}

name = input("Enter student's name: ")
if name in student_data:
    print(f"{name}'s marks: {student_data[name]}")
else:
    print("Student not found")

