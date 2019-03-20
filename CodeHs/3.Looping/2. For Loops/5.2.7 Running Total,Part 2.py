"""
This program first asks the user how many numbers they want to total. It then
asks them for that many numbers and reports the total of the numbers.
"""

total = 0
number_of_numbers = int(input("How many numbers would you like to sum? "))

# Repeat the code the number of times indicated by the user
for i in range(number_of_numbers):
    next = int(input("Enter a number: "))
    total = total + next

print("Sum: " + str(total))
