# Lir-Wan Fan
# Purpose: Creating a number guessing game.
# Randomly choose a number between 1 and 100 (inclusive)
# Have the player enter a guess via input
# Tell the player the guess is high, low, or correct
# If high or low, allow the player to enter another guess
# Give the player an option to quit at any time
# Reward the player for a correct guess (ex., "Good job!")
# Tell the player how many guesses it took to guess correctly

######################################################
# Randomly choose a number between 1 and 100 (inclusive)
import random
random_number = random.randint(1, 100)
print(f"Randomly chose a number between 1 and 100 and this number will be unknown to the player: {random_number}")
print("-------------------------------------------------------------------------------------------")
print("We have selected a number between 1 and 100.")

# Guess count for telling the player how many guesses it took to guess correctly
guess_count = 0

# Have the player enter a guess via input
while True:
    guess_number = input("Type in your guess number between 1 and 100 or 'q' to quit: ")

    try:
        guess_number = int(guess_number)
        guess_count += 1

        # Tell the player the guess is between 1 and 100
        if guess_number < 1 or guess_number > 100:
            print("The guess must be between 1 and 100.")
            print()
            continue

        # Tell the player the guess is too low
        if guess_number < random_number:
            print("Your guess is too low. Go up a little.")
            print()

        # Tell the player the guess is too high
        elif guess_number > random_number:
            print("Your guess is too high. Go down a little.")
            print()


        # Tell the player the guess is correct and reward the player for a correct guess
        # Tell the player how many guesses it took to guess correctly
        else:
            print(f"Good Job!! Congratulations!! You are the winner. It took you {guess_count} guesses.")
            break

    except ValueError:

        if guess_number.lower() != 'q':
            print("Invalid input!")

        # Give the player an option to quit at any time
        if guess_number.lower() == 'q':
            print(f"Thank you very much. You took {guess_count} guesses. Better luck next time. Goodbye!")
            break



