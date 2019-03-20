
def retrieve_positive_number():
    while(True):
        try:
            x = int(input())
        except ValueError:
            print("An error has occured")
        if(x>0):
            return x
        else:
            print("The value is not a zero")
                

retrieve_positive_number()
        
            
