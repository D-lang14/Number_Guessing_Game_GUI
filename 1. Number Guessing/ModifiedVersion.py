# ----------------------------------------------------Modified version of Number Guessing Game----------------------------------------------------

import random
import math

# Defining a funtion
def numberGuessingGame ():

    # Handling errors
    try:
        # Range is given by user
        rng1 = int(input("Enter lower bound: "))
        rng2 = int(input("Enter upper bound: "))

        # Generating random numbers between the range given by user
        randm = random.randint(rng1, rng2)
        print("\n\tYou've only ", round(math.log(rng2 - rng1 + 1, 2)), " chances to guess the integer!\n")

        # Initialization
        count = 0

        # chances of guessing no. restricted to 5 times
        while count < math.log(rng2 - rng1 + 1, 2):

            # Counting guesses
            count += 1

            # Taking input of guess
            guess = int(input("Enter your guess: "))
            

            if randm == guess:
                print("\n\tCongratulations! You took", count, "atempts")
                # Once guess is correct then it should break here
                exit(0)

            # Giving hints to the user
            elif randm < guess:
                print("\tYour guess is too high!")

            elif randm > guess:
                print("\tYour guess is too low!")

            else:
                print("Try Again")
                
            # If Guessing is more than required guesses
            if count >= math.log(rng2 - rng1 + 1, 2):
                print("\nThe number is %d" % randm)
                print("\tBetter Luck Next time!")
                exit(0)

        # This handles the empty input error
        int('')
    # error name
    except ValueError:
        print("\n Please Enter Proper Value \n")
        numberGuessingGame()
        
if __name__ == "__main__":
    # calling function
    numberGuessingGame()

# ----------------------------------------------------End of Program----------------------------------------------------
