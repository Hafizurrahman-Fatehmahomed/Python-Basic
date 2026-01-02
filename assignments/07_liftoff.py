#Problem Statement
#Write a program that prints out the calls for a spaceship that is about to launch. Countdown from 10 to 1 and then output Liftoff!
#Use a for loop to create the countdown.

import time

print("""People this is the day we were waiting for. The day of our lauch
Lets all count down together. Here we go:
""")
time.sleep(1)
for num in range(10, 0, -1):
  print(num)
  time.sleep(1)

print("Liftoff!")