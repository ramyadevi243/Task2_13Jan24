'''
Name: Ramya
Date: 16/01/2024
Problem Number: 3
'''

# Python program that takes a string and returns a new string with Vowels removed

# To input a string statement from user
string_statement = input("Please enter a string: ")

# Created a list of vowels and stored in variable called vowels
vowels = ['a','e', 'i', 'o', 'u', 'A','E', 'I', 'O', 'U']

# Created another variable called result that stores an empty string
result = ""

# Iterate over the string
for data in string_statement:
    
    # Using conditional statement and membership operator, check the elements
    # NOT present in list of vowels variable
    if data not in vowels:
        result = result + data
                
# Print the string after removing the vowels
print("After removing vowels, string will be: ",result)