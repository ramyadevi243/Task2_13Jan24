'''
Name: Ramya
Date: 16/01/2024
Problem Number: 2
'''
# To create pyramid of numbers from 1 to 20 using FOR loop

# Pattern 1
# Iteration of numbers in outer loop
for i in range (1, 21):
    # Iteration of numbers in inner loop
    for j in range(0, i):
        print(i,end="")
    # Print another line or shift to next line
    print()

# Pattern 2
# Iteration of numbers in outer loop
for i in range (1, 22):
    # Iteration of numbers in inner loop
    for j in range(1, i):
        print(j,end="")
    print()
