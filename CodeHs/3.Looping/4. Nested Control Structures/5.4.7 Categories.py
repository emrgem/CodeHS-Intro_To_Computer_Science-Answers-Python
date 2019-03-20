NumOfCatogories = 3
NumOfQuestion = 3
a = ["","",""]
for i in range(NumOfCatogories):
    catagoryName = str(input("Enter a category: "))
    for j in range(NumOfQuestion):
        a[j] = str(input("Enter something in that category: "))
    print(str(catagoryName)+": " + a[0] + " " + a[1] + " " + a[2])
