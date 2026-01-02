# Write a simple joke bot.
# The bot starts by asking the user what they want.
# However, the program will only respond to one response: "Joke".
#
# If the user enters "Joke" then we will print out a single joke.
# The joke is always the same:
#
# If the user enters anything else, we print out:
# Sorry I only tell jokes
#
# You should use the three constants:
# PROMPT, JOKE, SORRY
# which contain:
# - the prompt asked to the user,
# - the joke to print if the user enters "Joke",
# - and the sorry message for any other input.
#
# Your program needs to use an if statement that checks if the user input is "Joke":
# if user_input == "Joke":


joke = "Why do Python programmers prefer dark mode? Because the light attracts bugs!"
sorry = "Sorry, I only tell jokes"

def bot():
    user_input = input("How can I help you? ")  # Get user input
    if "joke" in user_input.lower():  # Check if 'joke' is in the input (case insensitive)
        print(joke)  # Print the joke
    else:
        print(sorry)  # Print sorry if no joke requested

bot()
