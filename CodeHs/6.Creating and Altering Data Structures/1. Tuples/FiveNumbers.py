
x = []
sum = 0
def create_list(a):
    x.append(a)

def ask_value():
    return int(input("Number: "))

for i in range(5):
    create_list(ask_value())
    print x

for i in x:
    sum += i

print sum