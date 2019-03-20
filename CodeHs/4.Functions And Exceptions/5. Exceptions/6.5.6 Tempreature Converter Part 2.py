def convert_C_to_F(c):
    f = ((1.8*c) + 32)
    return float(f)

# Now write your function for converting Fahrenheit to Celcius.

def convert_F_to_C(f):
    c = ((f-32) / 1.8)
    return float(c)

try:
    x = float(input())

except ValueError:
    print("An error has occured")

try:
    y = float(input())

except ValueError:
    print("An error has occured")


print(convert_C_to_F(x))

# Change 100C to F:
print(convert_C_to_F(y))
