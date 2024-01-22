'''
Name: Ramya
Date: 16/01/2024
Problem Number: 5
'''

# Python program that takes in a string and returns true if TRUE if it is a palindrome,
# false otherwise.

# To input a string from user
input_statement = input("Is This String a Palindrome? = ")

# Convert the input string into lowercase
result = input_statement.lower()

# Created another variable called empty_string
empty_string = ""

# Iterate over the input statement
for data in result:
    # Iterate through string and store each character in reverse and concatenate with the empty string
    empty_string = data + empty_string

# Conditional statement to check if the string is a palindrome or not using IF condition
if empty_string == result:
    print("TRUE")
else:
    print("FALSE")