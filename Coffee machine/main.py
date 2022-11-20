MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk":0,
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
def report():
    print(resources)

t1=True

def process(order):
    global t1
    a = resources["water"] - MENU[order]["ingredients"]["water"]
    b = resources["milk"] - MENU[order]["ingredients"]["milk"]
    c = resources["coffee"] - MENU[order]["ingredients"]["coffee"]

    if a <= 0:
        print("Out of water")
        t1= False
    elif b <= 0:
        print("Out of milk")
        t1= False
    elif c <= 0:
        print("Out of coffee")
        t1= False
    else:
        t1= True

def purchase():

    order=input("What would you like to have? e/l/c?: ")
    if order=='espresso':
        cost=MENU["espresso"]["cost"]
    elif order=='cappuccino':
        cost=MENU["cappuccino"]["cost"]
    elif order=='latte':
        cost=MENU["latte"]["cost"]
    elif order=='report':
        report()
        return
    else:
        print("wrong input")
        return

    process(order)

    while t1:
        quar=int(input("Enter no. of Quarters:"))
        dime=int(input("Enter no. of dimes:"))
        nick=int(input("Enter no. of nickels:"))
        cent=int(input("Enter no. of cents:"))

        money=quar*0.25+dime*0.1+nick*0.05+cent*0.01

        if money>=cost:
            print("Heres your order. enjoy")
            change=money-cost
            print(f"And your change: {change}")

            resources["water"] = resources["water"] - MENU[order]["ingredients"]["water"]
            resources["milk"] = resources["milk"] - MENU[order]["ingredients"]["milk"]
            resources["coffee"] = resources["coffee"] - MENU[order]["ingredients"]["coffee"]

        else:
            print("Not enough Money.")

        choice=input("Do you want to order again?y/n: ")
        if choice=='y':
            purchase()
        else:
            return

purchase()
