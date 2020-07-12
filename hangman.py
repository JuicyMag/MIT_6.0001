"""
MIT problem set 2 from FALL 2016 
I did get help online when I was stuck. The code is NOT exclusively my own work.
Credit to the following GitHub for their help:https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/


"""
# Problem Set 2, hangman.py
# Name: Magnus Herweyer 
# Collaborators: No one
# Time spent: start: 7/9/20 9:30am  - 

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

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
    print("  ", len(wordlist), "words loaded.")
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
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    for char in secret_word:
        if char not in letters_guessed:
            return False
    
    return True






def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
      
      
      Your initial hunch of needing to start with an empty string was CORRECT
      follow your intuition next time. 
    '''
    user_guess = ''
    a_e_i_o_u = 'a' or 'e' or 'i' or 'o' or 'u'
    
    """
        if char == a_e_i_o_u in secret_word:
            user_guess+= char
    """
   
    for char in secret_word:
        # if char == a_e_i_o_u in secret_word:
        #     user_guess+= char 
        if (char not in letters_guessed):
            user_guess+= '_ '
        else: 
            user_guess += char
           
    return user_guess        


            
# def contains_a_e_i_o_u(secret_word):
    
#     for char in secret_word:
#         if char == 'a' or 'i' or 'e' or 'o' or 'u':
            
    
    
    
#     return secret_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    
    available_letters= ''
    
    for char in string.ascii_lowercase:
        if char not in letters_guessed:
            available_letters += char
      
    return available_letters
    

def hangman(secret_word):

    
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is {} letters long".format((len(secret_word))))
  
            
    num_guesses = 6
    warnings_left =3
    letters_guessed = []
    print(secret_word)
    print(get_guessed_word(secret_word,letters_guessed))
    
    while True:  
        print('You have {} guesses left'.format(num_guesses))
     
        print('Available letters:{}'.format(get_available_letters(letters_guessed)))
        print(get_guessed_word(secret_word, letters_guessed))
        print("---------------------------------------------")
            
        letter_guessed = input('Input a letter:').lower()
        guessed_word = get_guessed_word(secret_word, letters_guessed)
        
        # Now we need to check to see if the input is in the alphabet
        
        if letter_guessed.isalpha():
            # isalpha = is in the alphabet 'abcde.....yz
            # Once we see if the input is a char, we have to see it hasn't been guessed already
            
            if letter_guessed not in letters_guessed:
                letters_guessed.append(letter_guessed)
                guessed_word = get_guessed_word(secret_word, letters_guessed)
            
                if letter_guessed in secret_word:
                    print('Good guess:{}'.format(guessed_word))
                    
                        
                if letter_guessed not in secret_word:
                        num_guesses -=1
                  
                 
                    
        else:
            if warnings_left >0:
                warnings_left-=1
                print("Oh shit! That is not a valid guess! Please enter a character")
            else:
                print("You have already entered that letter. You have {} warnings left. You will be penalized for guessing the letters already used: {}").format(warnings_left, guessed_word())
                warnings_left-=1
                    
        print("---------------------------------------------")
        
        # Used to tell the user that they won or lost and their score. We compute the score by seeing how many unique chars there are left in
        if is_word_guessed(secret_word, letters_guessed):
            num_unique_letters_inside_secret_word = []
            for char in secret_word:
                    if char not in num_unique_letters_inside_secret_word:
                        num_unique_letters_inside_secret_word.append(char)
            print("Congratulations! You won the game and I hope you enjoyed!")
            print("The word was: {}".format(secret_word))
            break
            
        if num_guesses == 0:
            print("No more guesses! Game over!")
            print("The word was: {}".format(secret_word))
            break
            




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
