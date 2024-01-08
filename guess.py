"""
    Do not run the script within the python intepreter, 
    just run the command("python guess.py") in a terminal, not in the interpreter.
"""

import random
import math

# taking inputs
lower = int(input("Please enter lower bound:- "))
upper = int(input("Please enter upper bound:- "))

# generating random number between the lower and upper
x = random.randint(lower, upper)
print("\n\t You've only ", round(math.log(upper - lower + 1, 2)),
      " chances to guess the integer! \n")

# initializing the number of guesses.
count = 0

# for calculation of minimum number of guesses depends upon range
while count < math.log(upper - lower + 1, 2):
    count += 1

    guess = int(input(" Guess a number:- "))

    # condition testing
    if x == guess:
        print("Congrats!, you did it ", count, " try")
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You guessed too high!")

# if guessing is more than required guesses, show this output
if count >= math.log(upper - lower + 1, 2):
    print("\n The number is %d" % x)
    print("\n Better luck next time!")
