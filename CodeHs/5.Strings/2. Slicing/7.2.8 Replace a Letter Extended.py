def replace_at_index(a,b,c):
    newList = list(a)
    location = b
    newList[location] = c
    sentence = ""
    
    for i in range(len(newList)):
        sentence += newList[i]
    return sentence

x = input("Enter a word or phrase: ")
y = int(input("Enter an index value: "))
z = input("Enter the new letter: ")

print replace_at_index(x,y,z)