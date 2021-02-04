"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730395109"

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
lucky_number: int = randint(1,20)
if lucky_number < 10:
    if lucky_number < 5:
        print("A new challenge lies ahead")
    else:
        print("You will soon reep the benefits of your hardwork")
else:
    if lucky_number < 15:
        print("Make the most of the relationships in your life")
    else:
        print("You will come into a large sum of money")
print("Now, go spread positive vibes!")