# Write your code here
class Drink:
    def __init__(self, d_id, title, water, milk, beans, cups, price):
        self.d_id = d_id
        self.title = title
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.price = price

    def __repr__(self):
        return f"id:{self.d_id}, title:{self.title}, water:{self.water}," \
               f" milk:{self.milk}, beans:{self.beans}, " \
               f"cups:{self.cups}, money:{self.price}"


class CoffeeMachine:
    n = 0

    def __new__(cls, *args):
        if cls.n == 0:
            cls.n += 1
            return object.__new__(cls)

    def __init__(self, water, milk, beans, cups, money, state="Standby"):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money
        self.state = state

    def __str__(self):
        return f"The coffee machine has:\n" \
               f"{self.water} of water\n" \
               f"{self.milk} of milk\n" \
               f"{self.beans} of coffee beans\n" \
               f"{self.cups} of disposable cups\n" \
               f"${self.money} of money\n"

    def __repr__(self):
        return f"State:{self.state}, water:{self.water}," \
               f" milk:{self.milk}, beans:{self.beans}, " \
               f"cups:{self.cups}, money:{self.money}\n"

    def fill_water(self):
        if self.state == "Filling_water":
            print("\nWrite how many ml of water you want to add:")
            self.water += int(input())
            self.state = "Filling_milk"

    def fill_milk(self):
        if self.state == "Filling_milk":
            print("Write how many ml of milk you want to add:")
            self.milk += int(input())
            self.state = "Filling_beans"

    def fill_beans(self):
        if self.state == "Filling_beans":
            print("Write how many grams of coffee beans you want to add:")
            self.beans += int(input())
            self.state = "Filling_cups"

    def fill_cups(self):
        if self.state == "Filling_cups":
            print("Write how many disposable coffee cups you want to add:")
            self.cups += int(input())
            self.state = "Standby"
            print()

    def collect_money(self):
        if self.state == "Collecting_money":
            print(f'\nI gave you ${self.money}\n')
            self.money = 0
            self.state = "Standby"

    def make_coffee(self, drink):
        miss_list = []
        if self.water < drink.water:
            miss_list.append("water")
        if self.milk < drink.milk:
            miss_list.append("milk")
        if self.beans < drink.beans:
            miss_list.append("coffee beans")
        if self.cups < drink.cups:
            miss_list.append("disposable cups")
        if self.money < drink.price:
            miss_list.append("money")
        if not miss_list and self.state == "Verifying_stocks":
            self.water -= drink.water
            self.milk -= drink.milk
            self.beans -= drink.beans
            self.cups -= drink.cups
            self.money += drink.price
            print("I have enough resources, making you a coffee!\n")
        else:
            print(f"Sorry, not enough {', '.join(miss_list)}!\n")
        self.state = "Standby"


my_cm = CoffeeMachine(400, 540, 120, 9, 550)
espresso = Drink("1", "espresso", 250, 0, 16, 1, 4)
latte = Drink("2", "latte", 350, 75, 20, 1, 7)
cappuccino = Drink("3", "cappuccino", 200, 100, 12, 1, 6)

action = ""
while action != "exit":
    print("Write action (buy, fill, take, remaining, exit):")
    action = input()
    if action in ["buy", "fill", "take", "remaining", "exit"]:
        if action == "buy":
            my_cm.state = "Choosing_drink"
            action = ''
            while action not in ["1", "2", "3", "back"]:
                print("What do you want to buy? "
                      "1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
                action = input()  # wanted_drink
            if action in ["1", "2", "3"] and my_cm.state == "Choosing_drink":
                my_cm.state = "Verifying_stocks"
                if action == "1":
                    my_cm.make_coffee(espresso)
                elif action == "2":
                    my_cm.make_coffee(latte)
                else:
                    my_cm.make_coffee(cappuccino)
        elif action == "fill":
            my_cm.state = "Filling_water"
            my_cm.fill_water()
            my_cm.fill_milk()
            my_cm.fill_beans()
            my_cm.fill_cups()
        elif action == "take":
            my_cm.state = "Collecting_money"
            my_cm.collect_money()
        elif action == "remaining":
            print(my_cm)
        else:
            pass
