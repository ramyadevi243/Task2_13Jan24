'''
Name: Ramya
Date: 16/01/2024
Problem Number: 7
'''

# Python program that takes a string and returns the most frequent character in it.

# Input a string from user
string_statement = input("Please Enter A String: ")

# Created an empty dictionary to store all the key-value pairs
# where KEY is the characters and VALUE is the number of occurrences of that character
empty_dictionary = {}

# Iterate over the user input statement
for data in string_statement:
    # Check if the current character is in the dictionary
    if data not in empty_dictionary:
        # If the character is not in the dictionary, then we have to make an entry
        # in dictionary as character and value = 1
        empty_dictionary[data] = 1
        # # If the character is already present in the dictionary, then we have to
        # increment the value with 1
    else:
        empty_dictionary[data] += 1

# Print the most frequent character in the string
print(max(empty_dictionary, key=empty_dictionary.get))