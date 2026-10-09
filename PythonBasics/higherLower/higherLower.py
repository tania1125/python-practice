import random
import art 
from data import famous_people_db
correct_answer = "True"
score = 0

def HigherLower():
    optionA, optionB = random.sample(famous_people_db,2)
    answer = ""
    if (optionA["followers"] > optionB["followers"]):
        answer = "A"
    else:
        answer = "B"
    print(f"Compare A: {optionA["name"]}, a famous {optionA["profession"]}, from {optionA["country"]}\n{art.vs_logo}\nAgainst B: {optionB["name"]}, famous {optionB["profession"]}, from {optionB["country"]}")
    chosen_option = input("Who has more followers? Type 'A' or 'B': ").upper()
    if (chosen_option == answer):
        global score
        score += 1
        return True
    else:
        return False

# main program logic
print(art.logo)
while HigherLower():
    print("\n"* 20)
    print(art.logo)
print(f"Sorry, that's wrong. Final score: {score}")