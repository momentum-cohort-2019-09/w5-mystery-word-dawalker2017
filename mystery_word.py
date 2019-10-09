# Predetermined Python module, 'import' calls the module for use throughout the code.
import random
#==================================================================================================| Reading the File |==============================#
# Creating a function that reads the file.


def read_the_file(filename):
    with open(filename) as file:
        text = file.read()
        return make_list_from_text(text)

#==================================================================================================| Making a List of the Text |=====================#
# Creating a function that puts words into a list and trims any space around each word.


def make_list_from_text(every_word):
    all_words = every_word.split()
    return all_words

#==================================================================================================| Get a Random Word |=============================#
# Creating a function that picks a random word out of the list of words.


def get_word(list_of_words):
    random_word = random.choice(list_of_words)
    print(random_word)
    return random_word

#==================================================================================================| Guess a Letter |================================#
# Creating a function to allow the User to guess a letter and determine wether it is correct/incorrect.


def guess_a_letter(word):
    guessed_letter = input("Guess a Letter")
    print(guessed_letter)

#==================================================================================================#
# Define the function of "is currently playing this game".
    # Define current state of "is playing this game".
    # Define empty array(list) for correct guesses.
    # Define empty array(list) for incorrect guesses.

    # Create a while loop of previously defined state AND length of User's incorrect guesses.
    # Pass through the while loop: 'state_of_game' AND 'length of incorrect guesses' [less than] 'chosen number'...
    # Call the 'guess_letter' function as previously created.('word', 'incorrect_guesses', 'correct_guesses').


#==================================================================================================#
# "words" is delacred as 'read_the_file' function as created above.
words = read_the_file('words.txt')

# Calling the 'guess_a_letter' function on the 'get_word' function previously created.
guess_a_letter(get_word(words))
