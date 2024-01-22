'''
Name: Ramya
Date: 16/01/2024
Problem Number: 9
'''

# Python program that takes a string and returns the number of words in it

# Input a string by user
input_string = input("Enter the string: ")

# Assign a variable blank_space and initialize it with 0
blank_space = 0

# Iterate over the string
for data in input_string:
    
    # Using assignment operator, check the string to find black spaces
    if data == " ":
        # Append the variable count with 1 for every blank space
        blank_space = blank_space + 1

# Declare a variable Number_Of_Words
Number_Of_Words = blank_space + 1

# Print the total number of words in the string
print("Total number of words in the string are: ",Number_Of_Words)