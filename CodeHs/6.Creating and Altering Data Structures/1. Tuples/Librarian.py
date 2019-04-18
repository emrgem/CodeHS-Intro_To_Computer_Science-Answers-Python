x = []
def create_list(a):
    x.append(a)

def ask_value():
    return (input("Name: "))

for i in range(5):
    create_list(ask_value())

x.sort()
print x