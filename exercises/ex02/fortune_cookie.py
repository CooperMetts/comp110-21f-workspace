"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730336784"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint

# Begin your solution here...

print("Your fortune cookie says...")

x: int = randint(1, 10)
y: int = 4

if x > y:
    print("The love of your life is stepping into your planet this summer.")
else: 
    if x == 3:
        print("Your shoes will make you happy today.")
    else: 
        if x < y: 
            print("A short stranger will soon enter your life with blessings to share.")
        else: 
            print("You will travel to many exotic places in your lifetime.")

print("Now, go spread positive vibes!")
