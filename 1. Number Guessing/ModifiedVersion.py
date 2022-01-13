# Modified version of Number Guessing Game

import random

# Range is given by user
rng1 = int(input("Enter your first desired range: "))
rng2 = int(input("Enter your last desired range: "))

# Generating random numbers between the range given by user
randm = random.randint(rng1, rng2)

# Initialization
count = 0

# chances of guessing no. restricted to 5 times
while count < 5:

    # Counting guesses
    count += 1

    print('You Have 5 Chances To Guess')

    # Taking input of guess
    guess = int(input("Enter your guess: "))
    if randm == guess:
        print("congratulations! You took", count, "atempts")
        break

    # Giving hints to the user
    elif randm < guess:
        print("Your guess is too high!")

    elif randm > guess:
        print("Your guess is too low!")

    else:
        print("try again")


'''
Issues Need to Resolve 
1. Bymistakenly, instead of giving inputs pressed enter, so should not give error
2. We can vary chances according to range 
'''