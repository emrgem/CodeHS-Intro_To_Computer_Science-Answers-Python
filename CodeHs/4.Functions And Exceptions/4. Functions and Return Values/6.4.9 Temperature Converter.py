# Write your function for converting Celcius to Fahrenheit here.
# Make sure to include a comment at the top that says what
# each function does!

def convert_C_to_F(c):
    f = ((1.8*c) + 32)
    return float(f)

# Now write your function for converting Fahrenheit to Celcius.

def convert_F_to_C(f):
    c = ((f-32) / 1.8)
    return float(c)

# Now change 0C to F:
print(convert_C_to_F(0))

# Change 100C to F:
print(convert_C_to_F(100))

# Change 40F to C:
convert_F_to_C(40)

# Change 80F to C:
convert_F_to_C(80)
