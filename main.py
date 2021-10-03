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

def check_resource(order_ingredients):
    has_resource = True
    # item = MENU[order]
    # print(item)
    # itemCost = item['cost']
    # itemWater = item['ingredients']['water']
    # itemCoffee = item['ingredients']['coffee']
    # itemMilk = 0
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            has_resource = False;

    # if order != "espresso":
    #     itemMilk = item['ingredients']['milk']
    # print(f"{itemCost} {itemWater} {itemCoffee} {itemMilk}")
    #
    # if itemWater > resources["water"]:
    #     print("Sorry there is not enough water.")
    #     hasResource = False
    #
    # if itemCoffee > resources["coffee"]:
    #     print("Sorry there is not enough coffee.")
    #     hasResource = False
    #
    # if itemMilk > resources["milk"] and order != "espresso":
    #     print("Sorry there is not enough milk.")
    #     hasResource = False

    return has_resource

def process_coins(order):
    """Returns the total calculaor form coins inse"""
    print("Please insert coins.")
    item = MENU[order]
    itemCost = item['cost']

    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    total_input_money = 0.25*quarters + 0.1*dimes + 0.05 *nickles + 0.01*pennies
    return total_input_money
    # if total_input_money < itemCost:
    #     print("Sorry that's not enough money. Money refunded.")
    # else:
    #     print("Here is ${total_input_money - itemCost} in change.")
    #     print("Here is your {order} ☕️. Enjoy!")

def is_transaction_successful(money_received, drink_cost):
    """Return true if money is accepted or False if money is insufficient"""
    if money_received >=drink_cost:
        change = round(money_received - drink_cost,2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True
profit = 0

while is_on:
    userInput = input("What would you like? (espresso/latte/cappuccino):")

    exist = False
    if userInput == "off":
        is_on = False
    elif userInput == "report":
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']} ml")
        print(f"Money: ${profit}")
    else:
        drink = MENU[userInput]
        if check_resource(drink["ingredients"]):
            payment = process_coins(userInput)
            if is_transaction_successful(payment,drink["cost"]):
                make_coffee(userInput,drink["ingredients"])
