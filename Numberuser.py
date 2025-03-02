# #  We Are Making The Number Gussing With The User And Then Make It With Comupter Version 


# #  we will make in a function
# 
#  Importing The Random Tio et The Random Numbers

import random


def user_guessinggame():
    number_guess = random.randint(0,10) 
    # the Numbers will come from 0 to 10 
    # making attempts variable for in how many ateempts you have guessed 
    attempts = 0

    print("\nGuess A Number Between 0 And 10 !:")

    while True:
        user_guessing = int(input("Enter Your Number For Guessing !"))
        attempts += 1

        #  Running The If Else Statments !

        if  user_guessing < number_guess:
            print("Too Low Please Try Again !")
        elif user_guessing > number_guess:
            print("Too High Please Try Again !")
        else:
         print(f"\nCongratulations On Gussing Correct Number In {attempts} Atempts")

user_guessinggame()
