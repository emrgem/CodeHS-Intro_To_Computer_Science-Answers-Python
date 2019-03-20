def count_occurrences(a,b):
    counter = 0
    for checker in a:
        if(checker == b):
            counter+=1
    return counter

print count_occurrences("haaa","a")