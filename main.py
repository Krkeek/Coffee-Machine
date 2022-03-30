MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def pay():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    total_paid = quarters*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01
    if total_paid < MENU[user_input]["cost"]:
        return [False]
    else:
        pay_back = total_paid - MENU[user_input]["cost"]
        return [True, pay_back]


def print_report():

    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}g')
    print(f"Money: ${money}\n\n")


def sufficient_resources():
    milk = 1
    water = resources["water"] - MENU[user_input]["ingredients"]["water"]
    coffee = resources["coffee"] - MENU[user_input]["ingredients"]["coffee"]
    if user_input != "espresso":
        milk = resources["milk"] - MENU[user_input]["ingredients"]["milk"]

    if water < 0:
        return [False, "Water"]
    elif coffee < 0:
        return [False, "Coffee"]
    elif milk < 0:
        return [False, "Milk"]
    else:
        return [True]


def resources_adjustment():
    resources["water"] -= MENU[user_input]["ingredients"]["water"]
    resources["coffee"] -= MENU[user_input]["ingredients"]["coffee"]
    if user_input != "espresso":
        resources["milk"] -= MENU[user_input]["ingredients"]["milk"]


money = 0
machine_off = False

while not machine_off:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_input == "report":
        print_report()
    elif user_input == "off":
        machine_off = True
    else:
        enough_resources = sufficient_resources()
        if not enough_resources[0]:
            print(f"Sorry there is no enough {enough_resources[1]}")
        else:
            pay_accepted = pay()
            if pay_accepted[0]:
                num = "{:.2f}".format(pay_accepted[1])
                print(f"Here is ${num} in change")
                resources_adjustment()
                money += MENU[user_input]["cost"]
                print(f"Here is your {user_input}. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded")
