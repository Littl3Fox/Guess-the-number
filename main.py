import random

def guess(x):
    random_number = random.randint(1,x)
    guess=0 

    while guess != random_number:
        try:
            guess = int(input(f"Guess a number between 1 and {x}: "))
            if(guess < 1 or guess > x):
                raise ValueError("Number is not between the range!") 
        except ValueError as msg:
            print(msg)
        else:
            if guess < random_number:
                print("Sorry, guess again. Too low.")
            elif guess > random_number:
                print("Try again, too high!")
            else:
                 print("Yay, you did it!!")


        
       


guess(20)
