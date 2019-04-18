import math

def distance(point1, point2):
    # Your code here...
    xPlane = pow((point2[0]-point1[0]),2)
    yPLane = pow((point2[1]-point1[1]),2)
    result = math.sqrt(xPlane + yPLane)
    return result 

# This should print 5.0
print distance((1, 1), (4, 5))