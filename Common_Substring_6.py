'''
Name: Ramya
Date: 16/01/2024
Problem Number: 6
'''

# Python program that takes 2 strings and returns the longest common substring between them.

# Input 2 strings from user
input_string_1 = input("Enter the 1st string: ")
input_string_2 = input("Enter the 2nd string: ")

# Create a variable called sub_string
sub_string = ""

# Create another empty string called result
result = ""

# Iterate over 1st string
for data in input_string_1:
    # Check for the characters in 2nd string that are present in data
    if data in input_string_2:
        # If there are common characters in data, then append the string result with characters from data
        result = result + data

# Iterate over the string result
for data2 in result:
    # Check for the characters in result that are not present in data2
    if data2 not in sub_string:
        # Append sub_string with characters in data2
        sub_string = sub_string + data2

# Print the common substring between the 2 strings        
print("Common substring between the 2 strings: ",sub_string)
      
