numerator = int(input("Enter a numerator: "))
denominator = 0  # Initialize the denominator with 0

# Keep asking for the denominator until it's not zero
while denominator == 0:
    denominator = int(input("Enter denominator (non-zero): "))
    if denominator == 0:
        print("Denominator cannot be zero. Please enter a non-zero value.")

# Check if the division is even
if numerator % denominator == 0:
    print("Divides evenly!")
else:
    print("Doesn't divide evenly.")
