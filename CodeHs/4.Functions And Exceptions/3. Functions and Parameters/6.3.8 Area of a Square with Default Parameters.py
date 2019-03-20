def calculate_area(side_length=10):
    area = side_length*side_length
    print("The area of a square with sides of length "+ str(side_length) +" is "+ str(area))


side_length = int(input("Enter side length: "))

if(side_length>0):
    calculate_area(side_length)
else:
    calculate_area()


    
