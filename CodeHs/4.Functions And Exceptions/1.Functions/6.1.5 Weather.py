def sunny():
    print("On a sunny day, sandals are appropriate footwear.")

def rainy():
    print("On a rainy day, galoshes are appropriate footwear.")

def snowy():
    print("On a snowy day, boots are appropriate footwear.")

def invalid():
    print("An invalid option was selected.")


options = str(input("What is the weather? (sunny, rainy, snowy): ")) 

if(options=="sunny"):
    sunny()
elif(options=="rainy"):
    rainy()
elif(options=="snowy"):
    snowy()
else :
    invalid()
    
