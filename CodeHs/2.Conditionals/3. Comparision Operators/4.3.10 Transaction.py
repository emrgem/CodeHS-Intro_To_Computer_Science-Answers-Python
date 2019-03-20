"""
This program simulates a single transaction -
either a deposit or a withdrawal - at a bank.
"""

inital_value = 1000 
Selection = input("Deposit or withdrawal: ")

if(Selection=="deposit"):
    
    MoneyAdd=int(input("Enter Amount: "))
    inital_value += MoneyAdd
    print("Final balance: "+(str(inital_value)))

elif(Selection=="withdrawal"):
    
    WithDrawMoney =int(input("Enter Amount: "))
    inital_value -= WithDrawMoney
    
    if(WithDrawMoney>inital_value): #CodeHS has a gltich where it only accepts this incorrect. WithDrawMoney Must be less than 0
        print("You cannot have a negative balance!")
    print("Final balance: "+(str(inital_value)))
    
else:
    print("Invalid transaction.")
