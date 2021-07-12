import random
import os

os.system("cls")

words = []
chars_guessed = []

lang = 0

MSG = ["Choice a letter: ", "Guessed words: ", "Victory!\n", "Type anything to continue... "]

HANGMAN_SPRITES = ("""

   +---+
   |   |
       |
       |
       |
       |
 =========""", """

   +---+
   |   |
   O   |
       |
       |
       |
 =========""", """

   +---+
   |   |
   O   |
   |   |
       |
       |
 =========""", """

   +---+
   |   |
   O   |
  /|   |
       |
       |
 =========""", """

   +---+
   |   |
   O   |
  /|\  |
       |
       |
 =========""", """

   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
 =========""", """

   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
 =========""")

def selectNewWord():
    string = words[random.randint(0, len(words)-2)]
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
    print(MSG[1]+str(words)+"\n")
    print(stateString+"\n")
    if attempts > 2:
        if attempts > 4:
            if attempts > 6:
                if attempts > 8:
                    if attempts > 10:
                        if attempts > 12:
                            attempts = 6
                        else:
                            attempts = 5
                    else:
                        attempts = 4
                else:
                    attempts = 3
            else:
                attempts = 2         
        else:
            attempts = 1
    else:
        attempts = 0

    print(HANGMAN_SPRITES[attempts])


def run():
    attempts = 0
    guessed_words = 0
    foundLetter = False
    selected_word = selectNewWord()


    while True:
        drawState(chars_guessed, attempts, guessed_words)
        userInput = str(input(MSG[0]))
        if userInput != '':
            userInput = userInput[0].lower()
        else:
            continue

        for i in range(0,len(selected_word)):
            if userInput == selected_word[i]:
                chars_guessed[i] = selected_word[i]
                foundLetter = True

        if (userInput == "a" or userInput == "e" or userInput == "i" or userInput == "o" or userInput == "u") and lang == 1:
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
                    chars_guessed[i] = selected_word[i]
                    foundLetter = True
        
        if False not in chars_guessed:  # The hangman game was solved
            drawState(chars_guessed, attempts, guessed_words)
            print(MSG[2])
            input(MSG[3])
            os.system("cls")
            chars_guessed.clear()
            selected_word = selectNewWord()
            guessed_words += 1
            attempts = 0
            continue

        if not foundLetter:
            attempts += 1
        foundLetter = False
        if attempts > 12:
            break

    os.system("cls")
    print(HANGMAN_SPRITES[6])
    print("""   _____          __  __ ______    ______      ________ _____  
  / ____|   /\   |  \/  |  ____|  / __ \ \    / /  ____|  __ \ 
 | |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) |
 | | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  / 
 | |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \ 
  \_____/_/    \_\_|  |_|______|  \____/   \/   |______|_|  \_\ 
                                                               
                                                               """)
    input()

if __name__ == "__main__":
    os.system("cls")
    print("""  _    _          _   _  _____ __  __          _   _     _____          __  __ ______ 
 | |  | |   /\   | \ | |/ ____|  \/  |   /\   | \ | |   / ____|   /\   |  \/  |  ____|
 | |__| |  /  \  |  \| | |  __| \  / |  /  \  |  \| |  | |  __   /  \  | \  / | |__   
 |  __  | / /\ \ | . ` | | |_ | |\/| | / /\ \ | . ` |  | | |_ | / /\ \ | |\/| |  __|  
 | |  | |/ ____ \| |\  | |__| | |  | |/ ____ \| |\  |  | |__| |/ ____ \| |  | | |____ 
 |_|  |_/_/    \_\_| \_|\_____|_|  |_/_/    \_\_| \_|   \_____/_/    \_\_|  |_|______|
                                                                                      
                                                                                      """)
    print("Select a language to start\n")
    print("1 for English\n2 para Español\n")
    language_in = str(input())
    if language_in != '' and language_in[0] == "2":
        lang = 1
        MSG = ["Elije una letra: ", "Palabras adivinadas: ", "Ganaste!\n", "Escribe algo para continuar... "]
    else:
        lang = 0
    try:
        if lang == 0:
            with open("./Data/dataEN.hgm",'r',encoding="utf-8") as f:
                for line in f:
                    words.append(str(line))
        else:
            with open("./Data/dataES.hgm",'r',encoding="utf-8") as f:
                for line in f:
                    words.append(str(line))
    except FileNotFoundError:
        print("Words file could not be found...")
        input()
        exit()
    run()