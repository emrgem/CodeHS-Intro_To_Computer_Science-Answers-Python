def replace_char(word):
    
    x = list(word)
    sentence = ""
    for i in range(len(word)):
        if x[i] == 'i':
            x[i] = '!'
    
    for i in range(len(word)):
        sentence += x[i]
    return sentence

enter_text = input("Enter text: ")
print replace_char(enter_text)