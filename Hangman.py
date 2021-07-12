import random
import os

os.system("cls")

words = []
chars_guessed = []


def selectNewWord():
    string = words[random.randint(0, len(words))]
    string = string.rstrip(string[-1])
    for char in string:
        chars_guessed.append(False)

    return string


def drawState(guessed,attempts,words):
    stateString = ''
    for thing in guessed:
        if thing == False:
            stateString += '_'
        else:
            stateString += thing.upper()
        stateString += ' '
    
    os.system("cls")
    print("Guessed words: "+str(words)+"\n")
    print(stateString+"\n")
    print("Attempts: "+str(attempts)+"\n")


def run():
    attempts = 0
    guessed_words = 0
    foundLetter = False
    selected_word = selectNewWord()

    while True:
        drawState(chars_guessed, attempts, guessed_words)
        if False not in chars_guessed:  # The hangman game was solved
            drawState(chars_guessed, attempts, guessed_words)
            print("Victory!\n")
            input("Type anything to continue... ")
            os.system("cls")
            chars_guessed.clear()
            selected_word = selectNewWord()
            guessed_words += 1
            continue

        userInput = str(input("Choice a letter: "))
        if userInput != '':
            userInput = userInput[0].lower()
        else:
            continue

        for i in range(0,len(selected_word)):
            if userInput == selected_word[i]:
                if selected_word[i] != chars_guessed[i]:
                    chars_guessed[i] = selected_word[i]
                else:
                    foundLetter = True

        if userInput == "a" or userInput == "e" or userInput == "i" or userInput == "o" or userInput == "u":
            if userInput == "a":
                userInput = "á"
            elif userInput == "e":
                userInput = "é"
            elif userInput == "i":
                userInput = "í"
            elif userInput == "o":
                userInput = "ó"
            else:
                userInput = "ú"
                
            for i in range(0,len(selected_word)):
                if userInput == selected_word[i]:
                    if selected_word[i] != chars_guessed[i]:
                        chars_guessed[i] = selected_word[i]
                    else:
                        foundLetter = True
        
        if not foundLetter:
            attempts += 1
        foundLetter = False


if __name__ == "__main__":
    with open("./Data/data.txt",'r',encoding="utf-8") as f:
        for line in f:
            words.append(str(line))
    run()