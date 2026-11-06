import random
from dictionaryy import words

rocket_art = {
0: r"""
    /\
   /  \
  | () |
  |    |
 /|    |\
/_|____|_\
""",
1: r"""
    /\
   /  \
  | () |
  |    |
 /|    |\
/_|____|_\
  *    *
  *    *
""",
2: r"""
    /\
   /  \
  | () |
  |    |
 /|    |
/_|____|_
  *    *
  *    *
""",
3: r"""
   /\
  /  \
 | () |
 |    |
 |    |
 |____|
 *    *
 *    *
 """,
4: r"""
   /\
  /  \
 | () |
 | /  |
 |  \ |
 |____|
 )/\/\(
  \/\/
""",
5: r"""
      /\
     /  \
    | () |
   |  /  |
   | \   |
  |_____|
 (^)/\/\(^)
  ~~\/\/~~
""",
6: r"""
  \  |  /
 -- BOOM --
  /  |  \
""",
}


def show_rocket(wrong_guess):
    print("=====================")
    print(rocket_art[wrong_guess])
    print("======================")


def main():
    # pick a random word and make it uppercase
    answer = random.choice(words).upper()

    # this will make blank spaces for each letter
    display_word = ["_"] * len(answer) ## it is a list 

    # we will set the wrong guesses at 0 or stage at 0 (initial stage)
    wrong_guess = 0
    guessed_letters = [] ## to keep track of letters guessed by the player till now 

    while True:
        show_rocket(wrong_guess)
        print(" ".join(display_word)) # it will show it like this " _ _ _ _ " joins by spaces in between

        guess = input("Guess a letter: ").upper()

        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter one letter.")
            continue

        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        ## finally after all the checkpoints, the guessed letter is added to the list (correc, incorrect both)
        guessed_letters.append(guess)

        ## now here is the element of list which is the guess, is in the answer as well (character)
        if guess in answer:
            print("Correct!")
            
            ## now since the guessed letter is in the answer, we will check its position
            for i in range(len(answer)):
                if answer[i] == guess: ##this will find at which place the character given by user is there in the answer
                    display_word[i] = guess ##then it will replace the blank by that letter
        else:
            print("Wrong guess!")
            wrong_guess = wrong_guess + 1

        # player has guessed the whole word
        if "_" not in display_word:
            show_rocket(wrong_guess)
            print("Congratulations! You guessed the word:", answer)
            break

        # FINALLYYY WE WILL EXPLODEEE THE ROCKET AFTER 6 WRONG GUESSESSS BOOOOOOM
        if wrong_guess == 6:
            show_rocket(wrong_guess)
            print("You lost! The answer was:", answer)
            break


if __name__ == "__main__":
    main()

