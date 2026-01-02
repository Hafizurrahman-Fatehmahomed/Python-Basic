## Project - Create a Dice

# random module in python helps us to generate random numbers.
# This is a simple dice rolling simulator where we can set the limit of the dice.
import random

def roll_dice(limit = 6 ):
  return random.randint(1, limit)

# This is the default which we entered above with 6 as limit
print (roll_dice())

# Dice with 12 as a limit
print (roll_dice(12))

# Dice with 24 as a limit
print (roll_dice(limit=24))