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

money = 0


def resource_check(coffee):
    common_resources = []
    for item in MENU[coffee]["ingredients"]:
        common_resources.append(item)
    resource = 0
    enough_resources = True
    while enough_resources and resource < len(common_resources):
        required_resources = MENU[coffee]["ingredients"][common_resources[resource]]
        if resources[common_resources[resource]] < required_resources:
            print(f"Sorry, there is not enough {common_resources[resource]}.")
            enough_resources = False
            return False
        else:
            resource += 1

    return True


def coffee_machine():
    global money
    coffee_select = input("What would you like? (espresso/latte/cappuccino): ")
    # If user selects report, output system's resources and change

    if coffee_select != "espresso" and coffee_select != "latte" and coffee_select != "cappuccino" and coffee_select != "report":
        print("You have not selected an available option, please select again.")
        coffee_machine()

    if coffee_select == "report":
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: {money}")
        coffee_machine()

    # Check if the system has enough resources
    enough_resources = resource_check(coffee_select)
    if not enough_resources:
        coffee_machine()

    print("Please insert coins.")
    quarters_input = int(input("How many quarters?: "))
    dimes_input = int(input("How many dimes?: "))
    nickles_input = int(input("How many nickels?: "))
    pennies_input = int(input("How many pennies?: "))

    # Calculate the amount of change user put in system
    coin_input = (quarters_input * .25) + (dimes_input * .10) + (nickles_input * .05) + (pennies_input * .01)

    if coin_input < MENU[coffee_select]["cost"]:
        print("Sorry, that is not enough change.")
        coffee_machine()
    elif coin_input > MENU[coffee_select]["cost"]:
        change = round(coin_input - MENU[coffee_select]["cost"], 2)
        money += MENU[coffee_select]["cost"]
        print(f"Here is {change} in change.")
    elif coin_input == MENU[coffee_select]["cost"]:
        money += MENU[coffee_select]["cost"]

    coffee_resources = MENU[coffee_select]["ingredients"]

    for resource in coffee_resources:
        resources[resource] -= coffee_resources[resource]

    print(f"Here's your {coffee_select}, enjoy!")

    coffee_machine()


coffee_machine()

"""
Phase 1
1. Coffee machine is filled to a set amount of resources (water, milk, and coffee)
2. User selects which coffee they want 
3. User puts in their change into the coffee machine

Phase 2
4. Coffee machine determines if enough change was given to make the coffee
    4a. If there is not enough change given by the user, the coffee machine does not make coffee
5. Coffee machine then checks resources against the needs of the coffee to see if it has enough resources to make the coffee
    5a. If the coffee machine has enough resources to make the coffee, the machine makes the coffee and subtracts resources from its overall resources
    5b. If the coffee machine does not have enough resources to make the coffee, the machine does not make the coffee and tells the user which resource it does not have enough of.
6. The machine resets and asks user again what kind of coffee user wants
7. If user asks for a "report" of the machine's resources, the machine will output all of the resources it has available in  its system

"""
