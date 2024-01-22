'''
Name: Ramya
Date: 16/01/2024
Problem Number: 1
'''

# Python program to calculate total number of vowels in a string and count of each
# individual vowels in the particular string

# Given string
statement = "Guvi Geeks Network Private Limited"

# Initialize the following variables with 0
count_vowels = 0
count_a = 0
count_e = 0
count_i = 0
count_o = 0
count_u = 0

# Iterate over a string to count total number of vowels in string
for data in statement:
    if data == 'a' or data == 'e' or data == 'i' or data == 'o' or data == 'u':
        count_vowels = count_vowels + 1
# Print total number of vowels in the string
print("Number of vowels in the string: ",count_vowels)

# Iterate over a string to count number of vowel 'a' in string
for data in statement:
    if data == 'a':
        count_a = count_a + 1
print("Number of vowel 'a' in string: ",count_a)

# Iterate over a string to count number of vowel 'e' in string
for data in statement:
    if data == 'e':
        count_e = count_e + 1
print("Number of vowel 'e' in string: ",count_e)

# Iterate over a string to count number of vowel 'i' in string
for data in statement:
    if data == 'i':
        count_i = count_i + 1
print("Number of vowel 'i' in string: ",count_i)

# Iterate over a string to count number of vowel 'o' in string
for data in statement:
    if data == 'o':
        count_o = count_o + 1
print("Number of vowel 'o' in string: ",count_o)

# Iterate over a string to count number of vowel 'u' in string
for data in statement:
    if data == 'u':
        count_u = count_u + 1
print("Number of vowel 'u' in string: ",count_u)