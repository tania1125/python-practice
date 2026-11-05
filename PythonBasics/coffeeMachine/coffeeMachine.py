from menuIngredients import MENU
resources = {"water": 200,
                 "milk": 479,
                 "coffee": 400,}
Profit = 0


def coffeeMachine():
    global Profit
    global resources
    is_on = True
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    while is_on:
        if choice == "off":
            is_on = False
        elif choice == "report":
            print(f"Resources Available: ")
            print(f"Water: {resources['water']}")
            print(f"Milk: {resources['milk']}")
            print(f"Cofee: {resources['coffee']}")
            print(f"Money: {Profit}")

            is_on = False
        elif checkResources(choice):
            Amount = MENU[choice]["cost"]
            print(f"The Total Amount for the drink is, {Amount}$")
            Amount_credited = process_coins()
            if transaction(Amount_credited, choice):
                ordered_ingredients = (MENU[choice]["ingredients"])
                for item in ordered_ingredients:
                    resources[item] -= ordered_ingredients[item]
                print(f"Here is your {choice}. Enjoy!")
                is_on = False
        else:
            is_on = False
    coffeeMachine()
    
def process_coins():
    global Profit
    print(f"Coffee Machine accepts only quarters, dimes, nickles and pennies \n Please Insert coins: ")
    total = int(input("How many quaters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05 
    total += int(input("How many pennies: ")) * 0.01
    Profit += total
    return total

def checkResources(ordered_item):
    ordered_ingredients = (MENU[ordered_item]["ingredients"])
    for item in ordered_ingredients:
        if ordered_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True
           
def transaction(money_credited, selected_drink):
    global Profit
    Cost = MENU[selected_drink]["cost"]
    if money_credited > Cost:
        print(f"Here is ${round(money_credited - Cost, 2)} dollars in change.")
        return True
    elif money_credited < Cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif money_credited == Cost:
        Profit += money_credited
        return True
    

coffeeMachine()
