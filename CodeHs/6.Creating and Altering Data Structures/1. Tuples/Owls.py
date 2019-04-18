owl_detection = 0

sentence = (input().lower()).split()
word_detector = ["owls","owl","owl's","owl.","owls."]


for eachword in range(len(sentence)):
    for word_detection in range(len(word_detector)):
        if word_detector[word_detection] in sentence[eachword]:
            owl_detection+=1
            break

print owl_detection