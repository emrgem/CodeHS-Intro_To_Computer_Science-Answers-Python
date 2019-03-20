Age = int(input("Age: "))
BirthLocation = str(input("Born in the U.S.?(Yes/No): "))
Year = input("Years of Residency: ")

if((Age>=35) and (BirthLocation=="Yes") and (Year>=14)):
    print("You are eligible to run for president!")
else:
    print("You are not eligible to run for president.")
