import random
import hangman_words
import hangman_art

chosen_word = random.choice(hangman_words.word_list)
print(f"********************GAME STARTS********************")
print(hangman_art.logo[0])
placeholder = "" 
for i in chosen_word:
    placeholder += "_"
print(f"The number of words placeholder: {placeholder}")

lives = 6
guess_done_previously = ""
while lives != 0 and "_"  in placeholder:

    print(f"********************{lives}/6 LIVES LEFT********************")
    guess = input("Guess a letter: ").lower()
    
    while guess in guess_done_previously:
        print(f" You have already guessed {guess}")
        guess = input("Guess a letter again: ").lower()
        
    guess_done_previously += guess

    display = ""
    flag = 0
    
    for position, letter in enumerate(chosen_word):
        if guess == letter:
            display += letter
            flag = 1
        else:
            display += placeholder[position] 

    print(f"{display} ")
    placeholder = display

    if flag != 1:
        lives -= 1
        print(f"You guessed {guess}, thats's not in the word, You Lose a life")
    print(f"{hangman_art.stages[lives]}")
    

if lives == 0:
    print("********You Lost********")
    print(f"The word was {chosen_word}")
else:
    print("********Woohoo You Won!********")