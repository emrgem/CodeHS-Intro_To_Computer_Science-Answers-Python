x = input("Enter a string of lowercase letters: ")
end = False
v =  ["a","e","i","o","u","y"]

for l in v:
    if l in x:
        print "Contains a lowercase vowel!"
        end=True
        break
    
if(end==False):
    print "Doesn't contain a lowercase vowel."