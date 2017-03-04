# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : Arti
# Collaborators : <your collaborators>
# Time spent    : <total time>
# Date created: 2nd, 3rd March 2017
# Date Last updated:

import math
import random
import string
import re

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7
WILDCARD = '*'
END_OF_HAND = '!!'

SCRABBLE_LETTER_VALUES = {
    WILDCARD:0, 'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

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
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    score = 0
    
    try:
        # if word is not an empty string
        if(word != ''):
            word = word.lower()
            first_component = 0
            
            for char in word:
                first_component += SCRABBLE_LETTER_VALUES.get(char, 0)
                
            #print('first_component:', first_component)
            wordlen = len(word)
            second_component = 7*wordlen - 3*(n-wordlen)
            
            if(second_component < 1):
                second_component = 1
                
            #print('second_component:', second_component)
            score = first_component * second_component
            
    except:
        print('Something went wrong while calculating score...')
        
    return score

#print(get_word_score('app*e', 19))

#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand={}
    num_vowels = int(math.ceil(n / 3))
    hand[WILDCARD] = 1

    for i in range(1,num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    new_hand = hand.copy()
    #print('word:', word)
        
    try:
        for char in word.lower():
            #print('char:', char, 'new_hand:', new_hand)
            
            # check if letter is present in hand
            if(char in new_hand.keys() and new_hand[char] > 0):
                new_hand[char] -= 1
                
                # if integer count of letter is 0, delete that element
                if(new_hand[char] == 0):
                    del(new_hand[char])
                
    except:
        print('Something went wrong while Update a hand by removing letters...')
    
    #print('new_hand:', new_hand)    
    return new_hand

#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    is_valid = True
    word = word.lower()
    new_hand = hand.copy()
    
    try:
        # check for wildcard
        if WILDCARD in word:
            new_word_is_valid = False
            
            # replace wildcard with vowel
            for vowel in VOWELS:
                new_word=word.replace(WILDCARD, vowel)
                
                # check validity of new word
                if new_word in word_list:
                    new_word_is_valid = True
            
            # if no new word id valid, set is_valid false
            if not new_word_is_valid:
                is_valid = False
        # if wildcard is not used
        else: 
            # check if word is not in word_list
            if word not in word_list:
                is_valid = False
        
        # check word is entirely composed of letters in the hand 
        if is_valid:
            for char in word:
                if(char in new_hand.keys() and new_hand[char] > 0):
                    new_hand[char] -= 1        
                else:
                    is_valid = False
                    break
            
    except:
        print('Something went wrong while Testing word validity...')
    
    return is_valid
#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    handlen = 0
    
    try:
        handlen = len(hand)
    except:
        print('Something went wrong while calculating length of current hand...')
    
    return handlen


def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
    
    # Keep track of the total score
    total_score = 0
    word = ''
    try:
        n = calculate_handlen(hand)
        # As long as there are still letters left in the hand:
        while n > 0:
            # Display the hand
            print('Current Hand: ')
            display_hand(hand)
            # Ask user for input
            word = input('Enter word, or "{}" to indicate that you are finished: '.format(END_OF_HAND))
            
            # If the input is two exclamation points:
            if word == END_OF_HAND:
                break
                # End the game (break out of the loop)
            # Otherwise (the input is not two exclamation points):
            else:  
                # If the word is valid:
                if is_valid_word(word, hand, word_list):
                    # Tell the user how many points the word earned,
                    # and the updated total score
                    score = get_word_score(word, n)
                    total_score += score
                    print('"{}" earned {} points. Total: {} points'.format(word, score, total_score))
                # Otherwise (the word is not valid):
                else:
                    # Reject invalid word (print a message)
                    print('That is not a valid word. Please choose another word.')
                    
                # update the user's hand by removing the letters of their inputted word
                hand = update_hand(hand, word)
                n = calculate_handlen(hand)
        # Game is over (user entered '!!' or ran out of letters),
        # so tell user the total score
        if calculate_handlen(hand) == 0:
            print('Ran out of letters.')
        
        print('Total score for this hand:', total_score)
    except:
        print('Something went wrong while Playing hand...')
    # Return the total score as result of function
    return total_score

#word_list = load_words()
##handOrig = {'a': 1, 'j': 1, 'e': 1, 'f': 1, 'r': 1, '*': 1, 'x': 1}
#handOrig = {'a': 1, 'c': 1, 'i': 1, 'f': 1, 't': 1, '*': 1, 'x': 1}
#score = play_hand(handOrig, word_list)
#
# Problem #6: Playing a game
# 


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    try:
        if letter in hand.keys():
            #print('hand:', hand)
            exclude_letters = '[^' + ''.join(hand.keys()) + ']'
            #print('exclude_letters:', exclude_letters)
            new_letter_set = ''.join(re.findall(exclude_letters, VOWELS + CONSONANTS))
            #print('new_letter_set:', new_letter_set)
            new_letter = random.choice(new_letter_set)
            hand[new_letter] = hand[letter]
            #print('new_letter:', new_letter,'hand:', hand)
            del(hand[letter])
            #print('new hand:', hand)
    except:
        print('Something went wrong while substituting a letter in the hand...')    
    
    return hand
 
#hand = substitute_hand({'a': 1, 'c': 1, 'i': 1, 'f': 1, 't': 1, '*': 1, 'x': 1}, 't')
#print('new hand:', hand)
    
def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    # total series score
    total_score = 0
    last_hand = {}
    is_substituted = False
    is_replay = False
    last_hand_score = 0
    
    try:
        # get total number of hands
        no_hands = int(input('Enter total number of hands: '))
        i = 0
        
        while i < no_hands:
            i += 1
            is_current_repeated_hand = False
            # Replay hand logic
            if last_hand != {} and not is_replay:
                replay = input('Would you like to replay the hand? (Yes/No) ')
                
                if replay.lower() == 'yes':
                    hand = last_hand.copy()
                    is_replay = True
                    is_current_repeated_hand = True
                    i -= 1
                else:
                    hand = deal_hand(HAND_SIZE)
            else:
                hand = deal_hand(HAND_SIZE)
            
            if not is_substituted and not is_current_repeated_hand:
                print('Current Hand: ') 
                display_hand(hand)
            
            # letter substitute logic
            if not is_substituted and not is_current_repeated_hand:
                sub_letter = input('Would you like to substitute a letter? (Yes/No) ')
                
                if(sub_letter.lower() == 'yes'):
                    letter = input('Which letter would you like to replace: ')
                    hand = substitute_hand(hand, letter)
                    is_substituted = True
            
            last_hand = hand.copy()
            
            score = play_hand(hand, word_list)
            
            # logic for repeated hand
            if is_current_repeated_hand:
                total_score -= last_hand_score
                
                if score < last_hand_score:
                    score = last_hand_score
            
            # Accumulates the score for each hand into a total score
            total_score += score
            last_hand_score = score
            print('----------------------------------------------------------------------')
        
        print('Total score over all hands:', total_score)
    except:
        print('Something went wrong while Playing game...')
        
    return total_score

#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)