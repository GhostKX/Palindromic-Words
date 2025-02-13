

# Logic for checking if the word is palindromic or not
while True:
    word = input('Please, type in a word to check or "Quit" to exit: ')
    if word.isalpha():
        word = word.upper()
        reversed_word = word[::-1]
        if word == 'QUIT':
            print('\nExit')
            exit(0)
        elif word == reversed_word:
            print('\nThis is palindromic word!')
            print(f'Version in backwards of word "{word}" is <"{reversed_word}">\n')
        else:
            print('\nThis is not palindromic word!')
            print('Inital word: "{}"'.format(word))
            print('Reversed version: "{}"\n'.format(reversed_word))
    else:
        print('\nError, unknown symbol')



