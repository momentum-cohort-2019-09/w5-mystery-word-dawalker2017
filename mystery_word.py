# Predetermined Python module, 'import' calls the module for use throughout the code.
import random

#==================================================================================================| READ FILE |=====================================#
# Creating a function that reads the file.


def read_the_file(filename):
    with open(filename) as file:
        text = file.read()
        return make_list_from_text(text)

#==================================================================================================| MAKE TEXT INTO LIST |===========================#
# Creating a function that puts words into a list and trims any space around each word.


def make_list_from_text(every_word):
    all_words = every_word.split()
    return all_words

#==================================================================================================| NEW GAME |======================================#
# Creating a function that displays the 'starting new game' introduction.


def new_game():
    starting_input = input(
        "\n               ?¿? MYSTERY WORD ?¿? \n Guess a letter to complete the word, Press 'ENTER' to start! \n")
    if starting_input == "":
        difficulty_level = input(
            "SELECT DIFFICULTY: e = Easy, m = Medium, h = Hard").lower()
        if difficulty_level == "e":
            print("EASY MODE")
        if difficulty_level == "m":
            print("MEDIUM MODE")
        if difficulty_level == "h":
            print("HARD MODE")
    else:
        print("Need Valid Input")
    return difficulty_level

#==================================================================================================| GET RANDOM WORD/REPLACE LETTERS |===============#
# Creating a function that picks a random word out of the list of words and replaces its letters with " _ ".


def get_word(list_of_words):
    random_word = random.choice(list_of_words).lower()
    current_word = (("[ _ ] ") * len(random_word))
    print("=== " + current_word + "===")
    print(random_word + '\n')
    return(random_word)

#==================================================================================================| DIFFICULTY |====================================#


def word_level(words, difficulty):
    easy = []
    moderate = []
    hard = []

    for word in words:
        if len(word) >= 4 and len(word) <= 6:
            easy.append(word)
        elif len(word) > 6 and len(word) <= 8:
            moderate.append(word)
        elif len(word) > 8:
            hard.append(word)
    if difficulty == "e":
        index = random.randrange(len(easy) + 1)
        return easy
    elif difficulty == "m":
        index = random.randrange(len(moderate) + 1)
        return moderate
    elif difficulty == "h":
        index = random.randrange(len(hard) + 1)
        return hard

#==================================================================================================| SHOW LETTERS |==================================#
# Creating a function that, if a guess of a letter is correct, then add it to the word. Otherwise, keep it a "_".


def display_letter(word, correct_guesses):
    display_word = " "
    for letter in word:
        if letter in correct_guesses:
            display_word += letter + " "
        else:
            display_word += "[ _ ]"
    print(display_word)
    return display_word

#==================================================================================================| GUESS LETTER/CORRECT OR INCORRECT |=============#
# Creating a function to allow the User to guess a letter and determine wether it is correct/incorrect.


def correct_or_incorrect_guess(word, correct_guesses, incorrect_guesses, lives):
    letter = input("Guess a Letter: ")
    if letter in word:
        correct_guesses.append(letter)
        print('\n' + "Correct!")
    else:
        incorrect_guesses.append(letter)
        lives -= 1
        print('\n' + "Try Again!")
        print(f" {lives} LIVES REMAINING")
    display_letter(word, correct_guesses)
    return correct_guesses, incorrect_guesses

#==================================================================================================| WINNING GAME |==================================#
# Creating a function that checks if the User has won the game yet.


def has_player_won(word, correct_guesses):
    for letter in word:
        if letter not in correct_guesses:
            return False
    return True

#==================================================================================================| GAME DURATION |=================================#
# Creating a function that uses a while loop that WHILE the 'game is playing' tracks number of incorrect guesses
# the users trys and after 10 is hit, the game ends


def during_game():
    currently_playing = True
    correct_guesses = []
    incorrect_guesses = []
    difficulty = new_game()
    word = get_word(word_level(read_the_file('words.txt'), difficulty))
    lives = 6

    while currently_playing and len(incorrect_guesses) < 6:
        correct_or_incorrect_guess(word, correct_guesses, incorrect_guesses, lives)
        if has_player_won(word, correct_guesses):
            currently_playing = False
            print("YOU WIN!")
    print("Game Over!")


#====================================================================================================================================================#
# "words" is delacred as 'read_the_file' function as created above.
during_game()
