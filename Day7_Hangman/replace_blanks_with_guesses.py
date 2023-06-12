# Step 1
import random

word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word = random.choice(word_list)

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: ").lower()

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

array_chosen_word = []

for letter in chosen_word:
    if letter == guess:
        array_chosen_word += letter
    else:
        array_chosen_word += "_"
print(f"the chosen word is {chosen_word} and the array is {array_chosen_word}")
