import random
import string

WORDLIST_FILENAME = "palavras.txt"


def load_words():
    """
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
    return random.choice(wordlist)


def is_word_guessed(secret_word, letters_guessed):
    secretLetters = []

#    for letter in secret_word:
#        if letter in secretLetters:
#            secretLetters.append(letter)
#        else:
#            pass

    for letter in secret_word:
        if letter in letters_guessed:
            pass
        else:
            return False

    return True


def get_guessed_word():

    guessed = ''

    return guessed


def get_available_letters():
    import string
    # 'abcdefghijklmnopqrstuvwxyz'
    available = string.ascii_lowercase

    return available


def remove_guess_from_avaliable_letters(letters_guessed):
    available = get_available_letters()

    for letter in available:
        if letter in letters_guessed:
            available = available.replace(letter, '')

    print 'Available letters', available


def alert_that_letter_already_guessed(letters_guessed):
    guessed = get_guessed_word()
    for letter in secret_word:
        if letter in letters_guessed:
            guessed += letter
        else:
            guessed += '_ '

    print 'Oops! You have already guessed that letter: ', guessed


def hangman(secret_word):
    guesses = 8
    letters_guessed = []
    print 'Welcome to the game, Hangam!'
    print 'I am thinking of a word that is', len(secret_word), ' letters long.'
    print '-------------'

    while is_word_guessed(secret_word, letters_guessed) == False and guesses > 0:
        print 'You have ', guesses, 'guesses left.'

        remove_guess_from_avaliable_letters(letters_guessed)

        letter = raw_input('Please guess a letter: ')

        if letter in letters_guessed:
            alert_that_letter_already_guessed(letters_guessed)

        elif letter in secret_word:
            # criar um metodo que alerta que o chute foi correto
            letters_guessed.append(letter)

            guessed = get_guessed_word()
            for letter in secret_word:
                if letter in letters_guessed:
                    guessed += letter
                else:
                    guessed += '_ '

            print 'Good Guess: ', guessed
        else:
            # criar um metodo que o chute foi incorreto
            guesses -= 1
            letters_guessed.append(letter)

            guessed = get_guessed_word()
            for letter in secret_word:
                if letter in letters_guessed:
                    guessed += letter
                else:
                    guessed += '_ '

            print 'Oops! That letter is not in my word: ',  guessed
        print '------------'

    else:
        if is_word_guessed(secret_word, letters_guessed) == True:
            print 'Congratulations, you won!'
        else:
            print 'Sorry, you ran out of guesses. The word was ', secret_word, '.'


secret_word = load_words().lower()
hangman(secret_word)
