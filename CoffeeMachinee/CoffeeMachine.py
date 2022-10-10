from CoffeeMachineLibrary import *


def process_money():
    user_quarters = int(input("How many quarters?"))
    user_dimes = int(input("How many dimes?"))
    user_nickles = int(input("How many nickles?"))
    user_pennies = int(input("How many pennies?"))
    return (user_quarters * 0.25) + (user_dimes * 0.10) + (user_nickles * 0.05) + (user_pennies * 0.01)


off = False
while not off:
    choice = input("  What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        off = True
    elif choice == "report":
        print(f'''Water: {resources["water"]}ml
Milk: {resources["milk"]}ml
Coffee: {resources["coffee"]}g
Money: ${resources["money"]} ''')
    else:
        if MENU[choice]["ingredients"]["water"] >= resources["water"]:
            print("Sorry there is not enough water.")
        elif MENU[choice]["ingredients"]["coffee"] >= resources["coffee"]:
            print("Sorry there is not enough coffee")
        elif MENU[choice]["ingredients"]["milk"] >= resources["milk"]:
            print("Sorry there is not enough milk")
        else:
            print("Please insert coins.")
            user_money = process_money()
            if user_money <= MENU[choice]["cost"]:
                print("Sorry that's not enough money. Money refunded")
            else:
                print(f'Here is ${user_money - MENU[choice]["cost"]} in change')
                print(f"Here is your {choice} ☕. Enjoy!")
                resources["water"] -= MENU[choice]["ingredients"]["water"]
                resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]
                resources["milk"] -= MENU[choice]["ingredients"]["milk"]
                resources["money"] += MENU[choice]["cost"]
