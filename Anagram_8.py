'''
Name: Ramya
Date: 16/01/2024
Problem Number: 8
'''
# Python program that takes a string and returns True if it is an anagram of another string.
# False otherwise.

# Defining 2 strings to check if they are anagrams
def anagram(statement_1, statement_2):
    # Changed both strings to lower case and
    # Removed the blank spaces between words of string, if any
    statement_1 = statement_1.lower().replace(" ", "")
    statement_2 = statement_2.lower().replace(" ", "")

    # Checking if length of both statements are equal
    # If not, then they are not anagrams
    if len(statement_1) != len(statement_2):
        return False
    
    # Creating an empty dictionary to store key-value pairs, with Key being th
    # characters of string and value being the frequency of occurrences in string
    character_count = {}

    # Iterate over the 1st string
    for data in statement_1:
        # Storing the value for each character as 1
        character_count[data] = character_count.get(data, 0) + 1
    # Iterating over the 2nd statement with characters from 1st statement
    for data in statement_2:
        # If characters from 1st statement is not present in 2nd statement
        # then they are not anagrams
        if data not in character_count or character_count[data] == 0:
            return False
        
        # Decrement the characters by 1 or remove characters from dictionary
        character_count[data] -= 1
        return True

# Input 2 strings from user
statement_1 = input("Please input 1st string: ")
statement_2 = input("Please input 2nd string: ")

# Call the function and check if 2 strings are anagram.
if anagram(statement_1, statement_2):
    print("The two strings are anagrams")
else:
    print("Not anagrams")