# Problem Set 2, hangman.py
# Name: Arti
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string
import re

WORDLIST_FILENAME = "words.txt"


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
    print(len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for char in secret_word:
        if char not in letters_guessed:
            return False
        
    return True

#secret_word = 'apple'
#letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
#print(is_word_guessed(secret_word, letters_guessed))

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guessed_word = []
    
    for char in secret_word:
        if char in letters_guessed:
            guessed_word.append(char)
        else:
            guessed_word.append('_ ')
    
    return ''.join(guessed_word)

#secret_word = 'apple'
#letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
#print(get_guessed_word(secret_word, letters_guessed))

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
#    available_letters = string.ascii_lowercase
#    
#    for char in letters_guessed:
#        available_letters = available_letters.replace(char, '')
#    
#    return available_letters

    #better way as string is non mutable, we can use list and then convert it into string
    available_letters = list(string.ascii_lowercase)
    
    for char in letters_guessed:
        #remove deletes first occurance, 
        #but we can use remove as each char will be present only one time
        available_letters.remove(char)
    
    return ''.join(available_letters)

#letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
#print(get_available_letters(letters_guessed))

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    print('Welcome to the game Hangman!\nI am thinking of a word that is {} letters long.\nYou need to guess one letter at a time.'.format(len(secret_word)))
    total_no_guesses = 6
    max_warnings = 3
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    #if secret_word length is equal to or greater than 5, then provide word length + 2 more guesses
    if(len(secret_word) >= total_no_guesses - 1):
        total_no_guesses = len(secret_word) + 2
    
    letters_guessed = []
    warnings_left = max_warnings
    unique_letters_in_secret_word = 0
    i = 0
    user_won = False
    print('You have {} warnings left.'.format(max_warnings))
    print('------------------------------------------------\n')
    
    while(i < total_no_guesses):
        print('You have {} guesses left.'.format(total_no_guesses - i))
        print('Available letters:', get_available_letters(letters_guessed))
        char = input('Please guess a letter: ')
        guessed_word = get_guessed_word(secret_word, letters_guessed)
        
        # valid letter
        if re.match('^[a-zA-Z]$', char) != None: #len(char) == 1 and (char in 'A-Za-z'):
            char = char.lower()
            
            # valid non-repeated letter
            if(char not in letters_guessed):
                letters_guessed.append(char)
                guessed_word = get_guessed_word(secret_word, letters_guessed)
                
                # letter present in secret_word
                if char in secret_word:
                    unique_letters_in_secret_word += 1
                    print('Good guess:', guessed_word)
                # letter not present in secret_word
                else:
                    print('Oops! That letter is not in my word:', guessed_word)
                    
                    # letter is vowel
                    if(char in vowels):
                        i +=2
                    # letter is consonant
                    else:
                        i += 1
                
                # check if all letters guessed
                if(is_word_guessed(secret_word, letters_guessed)):
                    print('------------------------------------------------\n')
                    print('Congratulations, you won!\nYour total score for this game is:', (total_no_guesses - i) * unique_letters_in_secret_word)
                    user_won = True
                    break
            # repeated lette
            else:
                if(warnings_left == 0):
                    i += 1
                    print("Oops! You've already guessed that letter. You have no warnings left\nso you lose one guess: {}".format(guessed_word))
                else:
                    warnings_left -= 1
                    print("Oops! You've already guessed that letter. You now have {} warnings left: {}".format(warnings_left, guessed_word))
        # invalid input
        else:
            if(warnings_left == 0):
                i += 1
                print("Oops! That is not a valid letter. You have no warnings left\nso you lose one guess: {}".format(guessed_word))
            else:
                warnings_left -= 1
                print('Oops! That is not a valid letter. You have {} warnings left: {}'.format(warnings_left, guessed_word))
            
        
        print('------------------------------------------------\n')

    if(not user_won):
        print("Sorry, you ran out of guesses. The word was '{}'.\nGame Over..".format(secret_word))

#secret_word = 'apple'
#hangman(secret_word)

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
