import random
import time
import requests
response=requests.get('https://api.datamuse.com/words?rel_jja=random')
words=[word['word']for word in response.json()]
word_to_guess=random.choice(words)
guessed_letters=[]
guessed_word=['_']*len(word_to_guess)
tries=6
print("Welcome to Hangman Game")
name=input("Enter your name:-")
print("Hello"+name+"!Best of Luck!")
print("The game is about to start!\nLet's play Hangman!")
print("I'm thinking of a word that is",len(word_to_guess),"letters long.")
while tries>0 and '_' in guessed_word:
    print(''.join(guessed_word))
    guess=input("Guess a letter:").lower()
    if len(guess) !=1:
        print("Please guess one letter at a time.")
    elif guess in guessed_letters:
        print("You already guessed that letter.Try again.")
    elif guess not in word_to_guess:
        print("Oops, that letter is not in my word.")
        tries-=1
        guessed_letters.append(guess)
    else:
        print("Good guess! That letter is in my word.")
        guessed_letters.append(guess)
        for i,letter in enumerate(word_to_guess):
            if letter == guess:
                guessed_word[i] = guess
if '_' not in guessed_word:
    print(' '.join(guessed_word))
    print("Congratulations, you won!")
else:
    print("Sorry, you ran out of tries. The word was", word_to_guess)
