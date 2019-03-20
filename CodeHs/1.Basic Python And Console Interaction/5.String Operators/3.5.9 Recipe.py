"""
This program asks the user for three ingredients,
three amounts, and a number of servings, and
determines how much of each ingredient is needed
to serve the specified number of servings.
"""

# Write program here...

ia = str(input("Enter ingredient 1: "))
ib = float(input("Ounces of "+ str(ia)))

ja = str(input("Enter ingredient 2: "))
jb = float(input("Ounces of "+ str(ia)))

ka = str(input("Enter ingredient 3: "))
kb = float(input("Ounces of "+str(ia)))
numserv = int(input("Number of servings: "))

print("Total ounces of " + ia + ": " + str((ib*numserv)))
print("Total ounces of " + ja + ": " + str((jb*numserv)))
print("Total ounces of " + ka + ": " + str((kb*numserv)))
