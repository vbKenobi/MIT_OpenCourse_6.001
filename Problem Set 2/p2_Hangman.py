"""
You will implement a function called hangman that will allow the user to play hangman
against the computer. The computer picks the word, and the player tries to guess
letters in the word.
1
Here is the general behavior we want to implement. Don’t be intimidated! This is just
a description; we will break this down into steps and provide further
functional specs later on in the pset so keep reading!
1. The computer must select a word at random from the list of available words
that was provided in words.txt
Note that words.txt contains words in all lowercase letters.
2. The user is given a certain number of guesses at the beginning.
3. The game is interactive; the user inputs their guess and the computer either:
a. reveals the letter if it exists in the secret word
b. penalize the user and updates the number of guesses remaining
4. The game ends when either the user guesses the secret word, or the user runs
out of guesses.
"""

import random
import string
import numpy as np

#Getting the txt file of words
WORDLIST_FILENAME = "Problem Set 2/words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


def is_word_guessed(secret_word, letters_guessed):
    #Function to determine if the all the secret word contains the letters guessed
    complete_word = True

    for x in secret_word:

        letter_found = False
        
        for y in letters_guessed:
            if(x == y):
                letter_found = True
                break
        
        if(not letter_found):
            complete_word = False
            break

    return complete_word

def get_guessed_word(secret_word, letters_guessed):
    modified_word = ""

    for x in secret_word:

        letter_found = False
        
        for y in letters_guessed:
            if(x == y):
                letter_found = True
                modified_word += y
                break
        
        if(not letter_found):
            modified_word += "_ "
            

    return modified_word

def get_avaliable_letters(letters_guessed):
    alpha = 0
    available = ""
    put_in_list = True

    for x in string.ascii_lowercase:

        put_in_list = True
        
        for y in letters_guessed:
            if x==y:
                put_in_list = False
                break
            
        if(put_in_list):
            available = available + string.ascii_lowercase[alpha]
        alpha += 1

    return available

def contains_letter(user_letter, secret_word):
    for x in secret_word:
        if(user_letter == x):
            return True
    
    return False

def num_unique_letters(secret_word):
    unique_letters = ""
    alphabet = string.ascii_lowercase
    counter = 0

    for x in secret_word:
        counter = 0
        for y in alphabet:
            
            if(x == y):
                unique_letters += x
                alphabet = alphabet[0: counter] + alphabet[counter+1: len(alphabet)] 
                counter += 1
                break
            else:
                counter += 1

    return len(unique_letters)

def remove_underscore(word):
    no_underscore = ""
    word = word.replace(" ", "")
    for x in range(len(word)):
        if(word[x] != "_"):
            no_underscore += word[x]

    return no_underscore


def start_game(secret_string):

    num_guesses = len(secret_string) + 2

    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_string), "characters long")
    print("-------------")

    return num_guesses

def is_valid_input(user_input, user_guesses, warnings, num_guesses):

    if(len(user_input) != 1):
        if(warnings > 0):
            warnings += -1
            print("You have already eneterd a guess that is more than one character, you have", warnings, "warnings remainging")
            return False, warnings, num_guesses
        else:
            num_guesses += -1
            print("You have entered a guess that is more than one character. You have zero warnings and you are loosing a guess, you have", num_guesses, "guesses left")
            return False, warnings, num_guesses

    if(contains_letter(user_input, user_guesses)):
        if(warnings > 0):
            warnings += -1
            print("You have already eneterd that guess, you have", warnings, "warnings remaining")
            return False, warnings, num_guesses
        else:
            num_guesses += -1
            print("You have already entered that guess. You have zero warnings and you are loosing a guess, you have", num_guesses, "guesses left")
            return False, warnings, num_guesses

    if(not(str.isalpha(user_input))):
        if(warnings > 0):
            warnings += -1
            print("You have eneterd a guess that is not a letter, you have", warnings, "warnings remaining")
            return False, warnings, num_guesses
        else:
            num_guesses += -1
            print("You have entered a guess that is not a letter. You have zero warnings and you are loosing a guess, you have", num_guesses, "guesses left")
            return False, warnings, num_guesses

    return True, warnings, num_guesses

def match_with_gaps(my_word, other_word, user_guesses):

    found_char = False 
    wrong = ""
    my_word = my_word.replace(" ", "")
    other_word = other_word.replace(" ", "")
    no_underscore = remove_underscore(my_word)

    for a in user_guesses:
        found_char = False
        for b in no_underscore:
            if(a == b):
                found_char = True
                break
        if(not found_char):
            wrong = wrong + a

    if(len(my_word) != len(other_word)):
        return False

    for x in range(len(my_word)):
        if(my_word[x] == "_"):
            for y in no_underscore:
                if(other_word[x] == y):
                    return False
        
        elif(my_word[x] != other_word[x]):
            return False

    for z in wrong:
        for j in other_word:
            if(z == j):
                return False
              
    return True

def show_possible_matches(my_word, wordlist, user_guesses):
    counter = 0
    list_of_words = []

    for x in wordlist:
        if(match_with_gaps(my_word, x, user_guesses)):
            list_of_words += [x]
            counter += 1
    if(counter == 0):
        print("No Matches Found")
    else:
        print(*list_of_words, sep = ", ") 


def hangman_iterations(num_guesses, user_guesses, wordlist, warnings, secret_string):

    print("You have", num_guesses, "guesses left")
    print("The avalaible letters are:", get_avaliable_letters(user_guesses))
    user_input = input("Please guess a letter: ")
    user_input = str.lower(user_input)

     

    if(user_input == "*"):
        show_possible_matches(get_guessed_word(secret_string, user_guesses), wordlist, user_guesses)
    
    else:
        bool_valid_input, warnings, num_guesses = is_valid_input(user_input, user_guesses, warnings, num_guesses)
        if(not bool_valid_input):
            print(get_guessed_word(secret_string, user_guesses))
            print("-------------")
        else:
            user_guesses += user_input
            if(contains_letter(user_input, secret_string)):
                print("Good Guess:" , get_guessed_word(secret_string, user_guesses))
            else:
                print("Oops! That letter isn't in my word:" , get_guessed_word(secret_string, user_guesses))
                if(contains_letter(user_input, "aeiou")):
                    num_guesses += -2    
                else:
                    num_guesses += -1
            print("-------------")

    return num_guesses, user_guesses, warnings


def Play_hangamn():
    wordlist = load_words()
    secret_string = choose_word(wordlist)
    user_guesses = ""
    warnings = 3
    num_guesses = start_game(secret_string)

    while(num_guesses > 0 and not is_word_guessed(secret_string, user_guesses)):
        num_guesses, user_guesses, warnings = hangman_iterations(num_guesses, user_guesses, wordlist, warnings, secret_string)
        
        if(is_word_guessed(secret_string, user_guesses)):
            print("Congratulations! You Won!")
            print("Your total score for this game is", num_guesses*num_unique_letters(secret_string))

        if(num_guesses <= 0):
            print("Sorry, you ran out of guesses! The word was", secret_string)
            break

continue_play = "y"

while(continue_play == "y"):
    Play_hangamn()
    continue_play = input("Would you like to play another game: ")
