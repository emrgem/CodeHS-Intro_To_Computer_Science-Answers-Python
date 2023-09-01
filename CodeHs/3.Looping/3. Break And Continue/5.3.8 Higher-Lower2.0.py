secret_float = 3.3312

while True:
    guess = float(input("Enter a guess: "))

    if round(guess, 2) < round(secret_float, 2):
        print("Too low!")
    elif round(guess, 2) > round(secret_float, 2):
        print("Too high!")
    else:
        print("Correct!")
        break
