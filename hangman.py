import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    return all(map(lambda i: i in lettersGuessed, list(secretWord))) 

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    output = []
    guessedList = map(lambda i: i in lettersGuessed, list(secretWord))
    for i in secretWord:
        output.append("_") 
    i = 0
    while i < len(guessedList): 
        if guessedList[i] == True:
            output[i] = list(secretWord)[i]
        i +=1
    return " ".join(output)

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alpha = list(string.ascii_lowercase)
    return "".join(sorted(list(set(alpha).difference(lettersGuessed))))

def hangman(secretWord):

    lettersGuessed = []
    letter = ''
    bar = '-------------'
    
    print 'Welcome to the game Hangman!'
    print 'I am thinking of a word that is %s letters long' % str(len(secretWord))
    print bar
    
    i = 8
    while i > 0:
        if isWordGuessed(secretWord, lettersGuessed) == True:
            return 'Congratulations, you won!'
            break
        
        print "You have %s guesses left." %i
        print "Available letters: %s" % getAvailableLetters(lettersGuessed)
        letter = str(raw_input("Please guess a letter:")).lower()

        if letter in lettersGuessed:
            print "Oops! You've already guessed that letter: %s" %getGuessedWord(secretWord, lettersGuessed)
            print bar
        if letter not in lettersGuessed and letter in secretWord:
            lettersGuessed.append(letter)
            print "Good guess: %s" %getGuessedWord(secretWord, lettersGuessed)
            print bar
        if letter not in secretWord and letter not in lettersGuessed:
            lettersGuessed.append(letter)
            print "Oops! That letter is not in my word: %s" %getGuessedWord(secretWord, lettersGuessed)
            print bar
            i-=1
        
    if i == 0:
        return 'Sorry, you ran out of guesses. The word was %s.' %secretWord
        

secretWord = chooseWord(wordlist).lower()
print hangman(secretWord)
