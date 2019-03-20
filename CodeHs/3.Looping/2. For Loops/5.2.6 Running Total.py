"""
This program asks the user for ten numbers. It then reports the total of the
ten numbers.
"""

# Variable to keep track of the running total
total = 0

# Ask the user fora value and add to total
for i in range(10):
    next = int(input("Enter a number: "))
    total = total + next

# Report the result
print "Sum: " + str(total)
