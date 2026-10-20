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
    "water": 100,
    "milk": 200,
    "coffee": 100,
}
money = 0
def print_report():
    print(f"Water: {resources["water"]}")
    print(f"Milk: {resources["milk"]}")
    print(f"Coffee: {resources["coffee"]}")
    print(f"Money: ${money}")


def resources_sufficient(order_ingredients):
    """Return True if there are enough resources to make the drink."""
    for item in order_ingredients:
        if order_ingredients[item] > resources.get(item, 0):
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    print(" please insert coins. thy should be quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01")
    quarters = int(input("How match quarters :"))
    dimes = int(input("How match dimes :"))
    nickles = int(input("How match nickles :"))
    pennies = int(input("How match pennies :"))
    total = ((0.25 * quarters) +( 0.10 * dimes) + (0.05 * nickles )+( 0.01 * pennies))
    return total

def its_enough(money_received, drink_cost):
    if money_received < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif money_received > drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        return True
    else:
        return True


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from resources to make the drink."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")


is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        is_on = False
    elif choice == "report":
        print_report()

    elif choice in MENU:
        drink_name = MENU[choice]
        if resources_sufficient(drink_name["ingredients"]):
            total = process_coins()
            drink = MENU[choice]["cost"]
            if its_enough(total,drink ):
                make_coffee(choice,drink_name["ingredients"])
                money +=drink

