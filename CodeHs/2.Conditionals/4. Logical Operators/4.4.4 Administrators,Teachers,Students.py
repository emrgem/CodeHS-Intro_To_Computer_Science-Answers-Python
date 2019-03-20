Type =input("Are you an administrator, teacher, or student?: ")

if(Type=="Administrators")or(Type=="teacher"):
    print("Administrators and teachers get keys! ")
elif(Type=="student"):
    print("Students do not get keys!")
else:
    print("You can only be an administrator, teacher, or student!")


