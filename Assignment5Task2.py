'''
Task 2: Demonstrate List Slicing
Problem Statement: Write a Python program that:
1.   Creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list
'''

num_list = []
# Create list of number from 1 to 10
for i in range(10):
    num_list.append(i + 1)

# Print original list
print(f'Original list: {num_list}')

# Get first five numbers into another list item and print that
list1 = num_list[0:5:1]
print(f'Extracted first five elements: {list1}')

# Reverse the extracted list and print
list1.reverse()
print(f'Reversed extracted elements: {list1}')
