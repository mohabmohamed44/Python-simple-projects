"""
The simple substitution cipher substitutes one letter from another. Since there is 26 possible substitution. 
A simple substitution caesar cipher has one to one translation for each symbol in cipher text.
"""

import random 

try:
    import pyperclip #pyperclip copies text from the clipboard
except ImportError:
    pass # If the pyperclip is not installed, don't do anything. it's not a big deal

# Every possible symbol that can be encrypted or decrypted

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    print(''' Simple substitution cipher has one to one translation for each letter in cipher text and for each symbol in plaintext''')

    # Let the user specify he wants to encrypt or decrypt 
    while True:
        print('Do you want to (e)ncrypt or (d)ecrypt? ')
        response = input('> ').lower()

        if response.startswith('e'):
            myMode = 'encrypt'
            break # break out of the loop if the user chooses to encrypts message
        elif response.startswith('d'):
            myMode = 'decrypt'
            break # break out of the loop if the user chooses to decrypt message and if the user did not choose encrypt or decrypt tell the user to enter a correct input
        print('please enter a letter (e) or (d).')
    
    # Let the user specify the key to specify:
    while True:
        print('please specify the key to use.')

        if myMode == 'encrypt':
            print('or enter RANDOM to have generated one for you')
        response = input('> ').upper()

        if response == 'RANDOM':
            myKey = generateRandomKey()
            print('The key is {}.KEEP THIS SECRET! '.format(myKey))
            break # break out of the loop if the user did what it should have done correctly without any error
        else:
            if checkKey(response):
                myKey = response
                break
    
    # Let the user specify the message to encrypt or decrypt
    print('Enter the message to {}.'.format(myMode))
    myMessage = input('> ')

    # preform the encryption / decryption:
    if myMode == 'encrypt':
        translated = encryptMessage(myMessage, myKey)
    elif myMode == 'decrypt':
        translated = 'decrypt'
        translated = encryptMessage(myMessage, myKey)

        # Display the results
        print('The %sed message is:' % (myMode))
        print(translated)

        try:
            pyperclip.copy(translated)
            print('Full text copied from the clipboard.' % (myMode))
        except:
            pass


def checkKey(key):
    keyList = list(key)
    letterList = list(LETTERS)
    keyList.sort()
    letterList.sort()
    if keyList != lettersList:
        print('There is an error in the key or symbol set.')
        return False
    return True

def encryptMessage(message, key):
    return translateMessage(message, key, 'decrypt')

def translateMessage(message, key, mode):
    translated = ''
    charsA = LETTERS
    charsB = key

    if mode == 'decrypt':
        charsA, charsB = charsB, charsA
    
    # Loop through each symbol in message:
    for symbol in message:
        if symbol.upper() in charsA:
            symIndex = charsA.find(symbol.upper())
            if symbol.upper():
                translated += charsB[symIndex].upper()
            else:
                translated += charsB[symIndex].lower()
        else:
            translated += symbol
    
    return translated

def generateRandomKey():
    key = list(LETTERS)
    random.shuffle(key)
    return ''.join(key)

# If this program was run (instead of imported), run the program:
if __name__ == '__main__':
    main()