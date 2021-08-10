def remaining(stocks):
    print("The coffee machine has:")
    for item in stocks:
        print(f"{stocks [item]} of {item}")
    print()


def fill_machine():
    global cm_state
    print("Write how many ml of water you want to add:")
    cm_state["water"] += int(input())
    print("Write how many ml of milk you want to add:")
    cm_state["milk"] += int(input())
    print("Write how many grams of coffee beans you want to add:")
    cm_state["coffee beans"] += int(input())
    print("Write how many disposable coffee cups you want to add:")
    cm_state["disposable cups"] += int(input())


def take_money():
    global cm_state
    print(f'I gave you ${cm_state["money"]}\n')
    cm_state["money"] = 0


def espresso():
    global cm_state
    cm_state["water"] -= 250
    cm_state["coffee beans"] -= 16
    cm_state["disposable cups"] -= 1
    cm_state["money"] += 4
    print("I have enough resources, making you a coffee!\n")


def latte():
    global cm_state
    cm_state["water"] -= 350
    cm_state["milk"] -= 75
    cm_state["coffee beans"] -= 20
    cm_state["disposable cups"] -= 1
    cm_state["money"] += 7
    print("I have enough resources, making you a coffee!\n")


def cappuccino():
    global cm_state
    cm_state["water"] -= 200
    cm_state["milk"] -= 100
    cm_state["coffee beans"] -= 12
    cm_state["disposable cups"] -= 1
    cm_state["money"] += 6
    print("I have enough resources, making you a coffee!\n")


def check_stocks(drink):
    global cm_state
    miss_list = []
    if drink == "1":  # espresso
        if cm_state["water"] < 250:
            miss_list.append("water")
        if cm_state["coffee beans"] < 16:
            miss_list.append("coffee beans")
        if cm_state["disposable cups"] < 1:
            miss_list.append("disposable cups")
        if cm_state["money"] < 4:
            miss_list.append("money")
        if not miss_list:
            espresso()
        else:
            print(f"Sorry, not enough {', '.join(miss_list)}!\n")
    if drink == "2":  # latte
        if cm_state["water"] < 350:
            miss_list.append("water")
        if cm_state["milk"] < 75:
            miss_list.append("milk")
        if cm_state["coffee beans"] < 20:
            miss_list.append("coffee beans")
        if cm_state["disposable cups"] < 1:
            miss_list.append("disposable cups")
        if cm_state["money"] < 7:
            miss_list.append("money")
        if not miss_list:
            latte()
        else:
            print(f"Sorry, not enough {', '.join(miss_list)}!\n")
    if drink == "3":  # cappuccino
        if cm_state["water"] < 200:
            miss_list.append("water")
        if cm_state["milk"] < 100:
            miss_list.append("milk")
        if cm_state["coffee beans"] < 12:
            miss_list.append("coffee beans")
        if cm_state["disposable cups"] < 1:
            miss_list.append("disposable cups")
        if cm_state["money"] < 6:
            miss_list.append("money")
        if not miss_list:
            cappuccino()
        else:
            print(f"Sorry, not enough {', '.join(miss_list)}!\n")


def make_coffee():
    global cm_state
    print("What do you want to buy? "
          "1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
    wanted_drink = input()
    if wanted_drink in ["1", "2", "3"]:
        check_stocks(wanted_drink)


def make_action(word):
    global cm_state
    if word == "buy":
        make_coffee()
    elif word == "fill":
        fill_machine()
    elif word == "take":
        take_money()
    elif word == "remaining":
        remaining(cm_state)
    else:
        pass


cm_state = {
    "water": 400,
    "milk": 540,
    "coffee beans": 120,
    "disposable cups": 9,
    "money": 550
}

action = ""
while action != "exit":
    print("Write action (buy, fill, take, remaining, exit):")
    action = input()
    if action in ["buy", "fill", "take", "remaining", "exit"]:
        make_action(action)
