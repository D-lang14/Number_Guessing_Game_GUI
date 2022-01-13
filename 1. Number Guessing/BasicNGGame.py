# ----------------------------------------------------Number Guessing Game----------------------------------------------------

# This was the basic program
# Where we have limited our conditions

# It's a module
import random  

# Generate a random number between 1 to 10
num = random.randint(1, 10) 

# Initialized a variable for guess inputs
flag = None

# It's an infinite loop
# Instead of any condition make it :: while True:
while (flag != num): 

    # Taking input from user
    flag = int(input("Enter your number between 1 to 10: "))

    # This condition is used to check if user input is correct or not
    if flag == num:
        print("Congratulation you won")
        # Here we used break because our loop is infinite
        break
    else:
        print("Oops, Try Again!!")

        
# ---------------------------------------------------- End of Program ----------------------------------------------------
