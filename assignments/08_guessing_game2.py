# Guessing Game 2
# In this assignment, we will create a guessing game where the user and the computer both choose a number.

import random

def guessing_game():
  computer_number = random.randint(1, 100)
  user_number = int(input("Please enter a number between 1 and 100 and our computer will also chose a number. Your number is: "))
  guess = str(input("Is the computers number lower or higher "))

  if user_number > computer_number:
    print(f"Amazing, you are correct. The computers number is higher than your number {computer_number}")

  else:
    print(f"The number was lower {computer_number}")

guessing_game()

