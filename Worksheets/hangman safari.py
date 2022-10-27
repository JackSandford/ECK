from random import randint
import re

print('>>> Safari hangman <<<')

wordlist = [
    'giraffe',
    'leopard',
    'cheetah',
    'ostrich',
    'buffalo',
    'meerkat',
    'vulture',
    'warthog',
    'gorilla',
    'gazelle'
]
splitlist = [
    'g i r a f f e',
    'l e o p a r d',
    'c h e e t a h',
    'o s t r i c h',
    'b u f f a l o',
    'm e e r k a t',
    'v u l t u r e',
    'w a r t h o g',
    'g o r i l l a',
    'g a z e l l e'
]

while True:
    imagelist = [
        ' .-\",',	  
        ' `~|| ' ,  	
        '   ||___',
        '   (\':.)`	',
        '   || ||	',
        '   || ||	',
        '   ^^ ^^	',
        '~~~~~~~~~~~~'
    ]
    for line in imagelist:
        print(line)

    choose = randint(0,7)
    secret_word = wordlist[choose]
    splitword = splitlist[choose]
    splitwordoriginal = splitword.split()
    split = splitword.split()
    wordlen = len(split)
    blank = '_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _'
    hiddenword = blank[:wordlen * 2]
    print(hiddenword)

    while True:
        guess = input('Guess a letter or the whole word: ').lower()
        if guess == secret_word:
            print('Congratulations, you have guessed the word')
            break
        elif guess == ('Help').lower():
            print('Enter a letter to guess a letter in the safari animal themed word \nor have a go at guessing the whole word.')
            continue
        elif guess in secret_word:
            if split.count(guess) == 1:
                position = splitwordoriginal.index(guess)  
                split.remove(guess)
                splitblank = hiddenword.split()
                splitblank[position] = guess
                hiddenword = ' '.join(splitblank)
                print(hiddenword)
            elif split.count(guess) > 1:
                while True:
                    if guess in split:
                        split.remove(guess)
                    else: break
                for pos in re.finditer(guess, secret_word):
                    s = pos.start()
                    splitblank = hiddenword.split()
                    splitblank[s] = guess
                    hiddenword = ' '.join(splitblank)
                    print(hiddenword)

                
        else:
            del imagelist[-2]
            for line in imagelist:
                print(line)
        if '_' not in hiddenword: 
            print('Congratulations, you have guessed the word')
            break
        if len(imagelist) == 1: 
            print('You have run out of guesses, the game is over')
            break
    while True:    
        yn = input('Would you like to play again? (Y/N): ').lower()
        if yn == 'y': 
            moveon = 0
            break
        elif yn == 'n': 
            moveon = 1
            break
        else: 
            print('Please enter either \'Y\' or \'N\'')
            continue
    if moveon == 0:
        continue
    elif moveon == 1:
        break
print('Thank you for playing')

#for letter in split:
#if letter == guess:
#del letter
