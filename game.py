import os
import csv
import random

game = True
clear = lambda: os.system('cls')
terminal_width = os.get_terminal_size()[0]

# Get words from csv file
def get_words():
    lst = []
    with open(os.path.join(os.sys.path[0], "words.csv"), mode='r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            lst.append(row)
    return lst

def print_centered(text):
    text = str(text)
    print(text.center(terminal_width))

def print_title():
    clear()
    print_centered('#############################')
    print_centered('########   Hangman   ########')
    print_centered('#############################')
    print()

# Prints parts of hangman depending on the round 
def print_hangman(round):
    linedict = {
        'line1': '',
        'line2': '',
        'line3': '',
        'line4': '',
        'line5': '',
        'line6': '',
        'line7': '',
        'line8': ''
    }
    if round > 0:
        linedict['line8'] = '######     '
    if round > 1:
        linedict['line2'] = '  #        '
        linedict['line3'] = '  #        '
        linedict['line4'] = '  #        '
        linedict['line5'] = '  #        '
        linedict['line6'] = '  #        '
        linedict['line7'] = '  #        '  
   
    if round > 2:
        linedict['line1'] = '  #######  '
        linedict['line2'] = '  #     #  '    
    if round > 3:
        linedict['line3'] = '  #     O  '
    if round > 4:
        linedict['line4'] = '  #    \|/ '
    if round > 5:
        linedict['line5'] = '  #    / \ '

    for key, val in linedict.items():
        print_centered(val)

# Gibt geheimes Wort mit unterstrichen oder den bereits erratenen Buchstaben aus
def print_secret_word(word, lets):
    hint_lst = ['_ ' for let in word]
    print_centered('Secret Word: ')
    print() 
    if len(lets) > 0:
        for letter in lets:
            for i in range(0, len(word)):
                if word[i] == letter:
                    hint_lst[i] = letter + ' '
    print_centered(''.join(hint_lst))
    print()


words = get_words()
secret_word = words[random.randint(0, len(words))][0].upper()
try_counter = 0
letters = []

while game:    
    print_title()
    print_hangman(try_counter)
    print('')
    print_secret_word(secret_word, letters)
    

    #  GET CORRECT INPUT 
    if try_counter < 6:
        print_centered('Type in Letter or Word: ')
        right_input = False
        while not right_input:
            user_input = input()
            if len(user_input) == 1 or len(user_input) == len(secret_word):
                right_input = True
            else:
                print_centered('Type in single letter or word that fits in the blank space!')

        if len(user_input) > 1:
            if user_input.upper() == secret_word.upper():
                print_centered('YOU WON!')
                print_centered(user_input.upper())
                print_centered('IS CORRECT!')
                game = False
                input()
            else:
                print_centered('WRONG!')
                print_centered('YOU LOOSE 1 Life!')
                try_counter += 1
        else:
            letters.append(user_input.upper())
            if not user_input.upper() in secret_word:
                try_counter += 1
    else:
        print_centered('You loose!')
        game = False
        input()
