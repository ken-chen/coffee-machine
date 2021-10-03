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

def check_resource(order):
    hasResource = True
    item = MENU[order]
    print(item)
    itemCost = item['cost']
    itemWater = item['ingredients']['water']
    itemCoffee = item['ingredients']['coffee']
    itemMilk = 0
    if order != "espresso":
        itemMilk = item['ingredients']['milk']
    print(f"{itemCost} {itemWater} {itemCoffee} {itemMilk}")

    if itemWater > resources["water"]:
        print("Sorry there is not enough water.")
        hasResource = False

    if itemCoffee > resources["coffee"]:
        print("Sorry there is not enough coffee.")
        hasResource = False

    if itemMilk > resources["milk"] and order != "espresso":
        print("Sorry there is not enough milk.")
        hasResource = False

    return hasResource

def process_coins(order):
    item = MENU[order]
    itemCost = item['cost']
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    total_input_money = 0.25*quarters + 0.1*dimes + 0.05 *nickles + 0.01*pennies

    if total_input_money < itemCost:
        print("Sorry that's not enough money. Money refunded.")
    else:
        print("Here is ${total_input_money - itemCost} in change.")
        print("Here is your {order} ☕️. Enjoy!")


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
        if check_resource(userInput):
            process_coins(userInput)
        # start()


# start()