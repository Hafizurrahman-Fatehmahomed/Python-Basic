# Guessing Game

# In this assignment, we will create a simple guessing game where the user has to guess a predefined number.

correct_number = 9
guess = 0

while guess != correct_number:
  guess = int(input("Guess the number "))
  print("Wrong, Try agan please" if guess != correct_number else "You guessed it right ")