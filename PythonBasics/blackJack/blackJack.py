from art import logo
import random
cards = [11, 2,3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def my_draw(my_hand, draws):
    my_hand.extend(random.sample(cards, draws))
    Initialmy_hand = my_hand
    return my_hand

def computer_draw(comp_hand, draws):
    comp_hand.extend(random.sample(cards, draws))
    return comp_hand

def win(myhand, comphand):
    myhand_score = sum(myhand)
    comphand_score = sum(comphand)
    print(f"Your final hand: {myhand}, final score: {myhand_score}")
    print(f"Computer's final hand: {comphand}, final score: {comphand_score}")
    print("You win")

def lose(myhand, comphand):
        myhand_score = sum(myhand)
        comphand_score = sum(comphand)
        print(f"Your final hand: {myhand}, final score: {myhand_score}")
        print(f"Computer's final hand: {comphand}, final score: {comphand_score}")
        print("You lose")

def draw(myhand, comphand):
        myhand_score = sum(myhand)
        comphand_score = sum(comphand)
        print(f"Your final hand: {myhand}, final score: {myhand_score}")
        print(f"Computer's final hand: {comphand}, final score: {comphand_score}")
        print("It's a Draw")

def checkScore(myhand, comphand):
    myhand_score = sum(myhand)
    comphand_score = sum(comphand)
    # if (myhand_score ==21 and len(myhand) == 2):
    #     return 0
    # elif(comphand_score ==21 and len(comphand) == 2):
    #         return 0
    if (myhand_score > 21):
        final_scenarios["You lose"](myhand,comphand)
    elif (comphand_score > 21):
        final_scenarios["You Win"](myhand,comphand)
    else: 
        if(myhand_score > comphand_score):
            final_scenarios["You Win"](myhand,comphand)
        elif(myhand_score < comphand_score):
            final_scenarios["You lose"](myhand,comphand)
        else:
            final_scenarios["Draw"](myhand,comphand)
        return False

final_scenarios = { "You Win": win, "You lose": lose, "Draw": draw }
comp_actions = {"Computer Draw Again": computer_draw, "Stand": "Staying with current hand"}

def BlackJack():
    game_start = input("Do you want to play a game of Blackjack ? Type'y' or 'n': ").lower()
    if game_start == 'y':
        print("\n"*20)
        print(logo)


        Initialmy_hand = []
        InitialComputer_hand = []
        no_of_draws = 2
        

        print(f"Your cards: {my_draw(Initialmy_hand, no_of_draws)}, current score: {sum(Initialmy_hand)}")
        print(f"Computer's first card {computer_draw(InitialComputer_hand, no_of_draws)[0]}")

        continue_drawing = True

        while continue_drawing:

            if sum(Initialmy_hand) > 21:
                checkScore(Initialmy_hand, InitialComputer_hand)
                break

            draw_again = input("Type 'y' to get another card, type 'n' to pass ").lower()

            if draw_again == 'y':
                no_of_draws = 1
                my_draw(Initialmy_hand, no_of_draws)
                print(f"Your cards: {Initialmy_hand}, current score: {sum(Initialmy_hand)}")
            elif draw_again == 'n':
                comp_choice = random.choice(list(comp_actions.keys()))
                # Computer evaluates if it wants to draw based on the random choice dictionary setup
                if comp_choice == "Computer Draw Again" and sum(InitialComputer_hand) < 17:
                    print("\nComputer chooses to draw again!")
                    comp_actions["Computer Draw Again"](InitialComputer_hand, 1)
                else:
                    print(f"\nComputer decides to: {comp_actions['Stand']}")

                continue_drawing = checkScore(Initialmy_hand, InitialComputer_hand)
        BlackJack()

BlackJack()