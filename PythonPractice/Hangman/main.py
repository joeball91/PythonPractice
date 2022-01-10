import random
import hangmanwordbank
from os import system

hangman_list = []
guessed_letters = []
word = random.choice(hangmanwordbank.word_list)
lives = 6

for x in range(len(word)):
    hangman_list += "_"

hangman_index = 0
system("clear")
print("\nWelcome to Hangman!")
print(hangmanwordbank.HANGMANPICS[hangman_index])
while lives > 0:
    count = 0
    exists = False
    guess = input("\nChoose a letter: ").lower()
    for x in range(len(word)):
        if guess == word[x]:
            hangman_list[x] = word[x]
            exists = True
        if hangman_list[x] == '_':
            count += 1       
    if count == 0:
        lives = -1

    if exists == False:
        if guess not in guessed_letters:
            guessed_letters += guess
            hangman_index += 1
            system("clear")
            print(hangmanwordbank.HANGMANPICS[hangman_index])
            print (f"\n\nGuessed letters: {guessed_letters}")
            print()
            print(hangman_list)
            lives -= 1
        else:
            system("clear")
            print(hangmanwordbank.HANGMANPICS[hangman_index])
            print(f"\n\nYou have already guessed {guess}")
            print (f"Guessed letters: {guessed_letters}")
            print()
            print(hangman_list)
    else:
        if guess not in guessed_letters:
            guessed_letters += guess
            system("clear")
            print(hangmanwordbank.HANGMANPICS[hangman_index])
            print (f"\n\nGuessed letters: {guessed_letters}")
            print()
            print(hangman_list)
        else:
            system("clear")
            print(hangmanwordbank.HANGMANPICS[hangman_index])
            print(f"\n\nYou have already guessed {guess}")
            print (f"Guessed letters: {guessed_letters}")
            print()
            print(hangman_list)

system("clear")
print(hangmanwordbank.HANGMANPICS[hangman_index])
print()
print(hangman_list)
if lives == 0:
    print(f"\nOh no. You lost! The word was {word}.\n")
else:
    print(f"\nGood job, you guessed {word}!\n")