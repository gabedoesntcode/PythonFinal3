import random
import time

def isValidWord(word):
    return len(word) == 5


def isCorrectWord(target, guess):
    if len(target) != len(guess):
        return False
    return all(target[i] == guess[i] for i in range(len(target)))


def containsLetter(target, letter):
    return any(c == letter for c in target)


def displayGuessedWord(target, guess):
    for i in range(len(target)):
        if target[i] == guess[i]:
            print(target[i], end='')
        elif containsLetter(target, guess[i]):
            print('+', end='')
        else:
            print('-', end='')
    print()


def isValidWord(word):
    return len(word) == 5 and word.isalnum()


def isCorrectWord(target, guess):
    return target == guess


def displayGuessedWord(target, guess):
    for i in range(len(target)):
        if target[i] == guess[i]:
            print(target[i], end="")
        else:
            print("_", end="")
    print()


words = [
    "ST4R3", "CL0UD", "P1NKY", "GR4P3", "L3M0N", "GR34T", "N0BL3", "GU3ST",
    "M0P3R", "TR1CK", "S4SSY", "C0D3R"
]

random.seed(time.time())

target = random.choice(words)
attempts = 6
print("Welcome to Wordle! Please Enter a 5-Letter Alphanumeric Word")
print("*Guesses Should Be Written In All Caps*")
print("Letter-To-Number Key: E=3, A=4, I=1, O=0")
while attempts > 0:
    guess = input("Enter your guess: ")

    if not isValidWord(guess):
        print("Invalid word. Please enter a 5-letter word.")
        continue

    if isCorrectWord(target, guess):
        print("Congratulations! You guessed the word:", target)
        break
    else:
        displayGuessedWord(target, guess)
        attempts -= 1
        print("Attempts remaining:", attempts)

if attempts == 0:
    print("Game Over. The word was:", target)
