def replace_at_index(a,b):
    x = list(a)
    x[b] = "-"
    sentence = ""
    for i in range(len(x)):
        sentence += x[i]
    return sentence

s = replace_at_index("eggplant", 3)
print s