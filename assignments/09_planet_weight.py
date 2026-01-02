# For this assignment, you will create a program that calculates a person's weight on different planets based on their weight on Earth.
# The program should prompt the user to enter their name, weight on Earth (in kg), and the planet they want to calculate their weight for.
# The program should then output the user's weight on the specified planet.

planets = {
    "Mercury" : 37.6,
    "Venus" : 88.9,
    "Mars" : 37.8,
    "Jupiter" : 236.0,
    "Saturn" : 108.1,
    "Uranus" : 81.5,
    "Neptune" : 114.0

}

def planet_weight():
  name = str(input("Please enter your name: ")).strip()
  weight = float(input("Please enter your weight in kg: "))
  on_which_planet = input("Which planet you on? ").strip().title()

  if on_which_planet not in planets:
    print(f"Sory {name}, we dont have date for {on_which_planet}.")
    return

  gravity = planets[on_which_planet]
  weight_on_planet = weight * (gravity / 100)

  print(f"Hello {name}! Your weight on {on_which_planet} would be {weight_on_planet:.2f} kg.")

planet_weight()
