'''
Name: Ramya
Date: 16/01/2024
Problem Number: 4
'''

# Python program that takes a string and returns the number of unique characters in it.

# Input a string from user
string_statement = input("Please Enter A String: ")

#Initialize an empty list: A list which does not have any values inside it
empty_list = []

#Iterate a for loop over the string
for data in string_statement:
    
    # Check if each character of given string is present in empty list.
    # If not present, then append the charecters to empty list
    if data not in empty_list:
        empty_list.append(data)
        
# Print the number of unique characters of the given string
print(len(empty_list))

# Print the unique characters of the given string
print(empty_list)