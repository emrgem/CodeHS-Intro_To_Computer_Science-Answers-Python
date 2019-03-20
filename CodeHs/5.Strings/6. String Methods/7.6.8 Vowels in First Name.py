name = input("What is your first name?:")

def vowels():
    
    print "There is an a in your name, first found at index " + str(name.find("a"))
    print "There is an e in your name, first found at index " + str(name.find("e"))
    print "There is an i in your name, first found at index " + str(name.find("i"))
    print "There is an o in your name, first found at index " + str(name.find("o"))
    print "There is an u in your name, first found at index " + str(name.find("u"))
    
vowels()