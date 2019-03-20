Age = int(input("Age: "))
BornLocation = str(input("Born in the U.S.?(Yes/No): "))
Year = input("Years of Residency: ")

if((Age>=35) and (BornLocation=="Yes") and (Year>=14)):
    print("You are eligible to run for president!")
else:
    print("You are not eligible to run for president.")
if(Age<35):
    print("You are too young. You must be at least 35 years old.")
if(BornLocation=="No"):
    print("You must be born in the U.S. to run for president.")
if(Year<14):
    print("You have not been a resident for long enough.")

