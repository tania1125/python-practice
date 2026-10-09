import random
from art import logo

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
num_to_find = random.randint(1, 100)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

def guess_loop(guess_left):
    while guess_left != 0:
        your_guess = int(input("Make a guess: "))
        if (your_guess > num_to_find):
            print("Too high")
            guess_left -= 1
        elif(your_guess < num_to_find):
            print("Too Low")
            guess_left -= 1
        else:
            print(f"You got it! The answer was {num_to_find}")
            break
        print(f"You have {guess_left} attempts remaining to guess the number")
    print(f"You've run out of guesses.The number was {num_to_find} re-run to play again")
        

if difficulty == 'easy':
    num_of_guess = 10
    print(f"You have {num_of_guess} attempts to guess the number")
    guess_loop(num_of_guess)

elif difficulty == 'hard':
    num_of_guess = 5
    print(f"You have {num_of_guess} attempts to guess the number")
    guess_loop(num_of_guess)

