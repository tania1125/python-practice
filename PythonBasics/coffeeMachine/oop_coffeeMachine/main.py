from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menuObj = Menu()
coffee_makerObj = CoffeeMaker()
moneyObj = MoneyMachine()
is_on = True

while is_on:

    options = menuObj.get_items()
    choice =  choice = input(f"What would you like? {options}: ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print("Resources Available:")
        coffee_makerObj.report()
        moneyObj.report()
    else: 
        drink = menuObj.find_drink(choice)
        if coffee_makerObj.is_resource_sufficient(drink):
            cost = drink.cost
            if moneyObj.make_payment(cost):
                coffee_makerObj.make_coffee(drink)
                

