from Day_15.coffee_menu import MENU, resources


# enable report production
def report(water_left, water_used, milk_left, milk_used, coffee_left, coffee_used, money_taken, customer_entry):
    total_money = money_taken
    remaining_water = water_left - water_used
    remaining_milk = milk_left - milk_used
    remaining_coffee = coffee_left - coffee_used
    return remaining_water, remaining_milk, remaining_coffee


# what the customer chooses
def customer_choice():
    entry = input("What would you like? (espresso, latte, cappuccino)").lower()
    while entry not in ("espresso", "latte", "cappuccino", "report", "off"):
        entry = input("Please enter a valid response.\nWhat would you like? (espresso, latte, cappuccino)").lower()
    return entry


# ingredients for the coffee chosen
def ingredients_for_choice(customer_entry):
    if customer_entry in MENU:
        water_used = MENU[customer_entry]["ingredients"]["water"]
        coffee_used = MENU[customer_entry]["ingredients"]["coffee"]
        if customer_entry == "espresso":
            milk_used = 0
        else:
            milk_used = MENU[customer_entry]["ingredients"]["milk"]
        print(water_used, milk_used, coffee_used)
        return [water_used, milk_used, coffee_used]


# check if there is enough stuff left
def check_resources(water, milk, coffee, money, customer_entry):
    water_left = water
    milk_left = milk
    coffee_left = coffee
    money_taken = money
    ingredients_needed = ingredients_for_choice(customer_entry)
    check_whats_left = report(water_left, ingredients_needed[0], milk_left, ingredients_needed[1], coffee_left,
                              ingredients_needed[2], money_taken, customer_entry)
    if check_whats_left[0] < 0:
        print("Not enough water left.")
        return False, water_left, milk_left, coffee_left, money_taken
    elif check_whats_left[1] < 0:
        print("Not enough milk left.")
        return False, water_left, milk_left, coffee_left, money_taken
    elif check_whats_left[2] < 0:
        print("Not enough coffee left.")
        return False, water_left, milk_left, coffee_left, money_taken
    else:
        print("Drink being made")
        water_left -= ingredients_needed[0]
        milk_left -= ingredients_needed[1]
        coffee_left -= ingredients_needed[2]
        return True, water_left, milk_left, coffee_left, money_taken


# run the coffee machine
def run_the_coffee_machine():
    machine_running = True
    water_left = resources['water']
    milk_left = resources['milk']
    coffee_left = resources['coffee']
    money_taken = 0
    while machine_running:
        customer_entry = customer_choice()
        if customer_entry == "off":
            machine_running = False
        elif customer_entry == "report":
            print(f"Water: {water_left}\nMilk: {milk_left}\nCoffee: {coffee_left}\nMoney: {money_taken}")
        else:
            can_it_be_made = check_resources(water_left, milk_left, coffee_left, money_taken, customer_entry)
            print(can_it_be_made)
            if not can_it_be_made[0]:
                print("Please make another choice.")
            else:
                water_left = can_it_be_made[1]
                milk_left = can_it_be_made[2]
                coffee_left = can_it_be_made[3]
                money_to_add = how_much(customer_entry)
                money_taken += money_to_add
                payment(money_to_add)


# how much does the customer owe
def how_much(customer_entry):
    if customer_entry in MENU:
        price = MENU[customer_entry]["cost"]
        return price


# how many coins has the customer entered, work out change
def payment(price):
    print(f"${price} to pay.")
    total_paid = 0
    while total_paid < price:
        quarters = int(input("How many quarters are you adding? "))
        nickels = int(input("How many nickels are you adding? "))
        dimes = int(input("How many dimes are you adding? "))
        pennies = int(input("How many pennies are you adding? "))
        total_paid = round((quarters * 0.25) + (nickels * 0.1) + (dimes * 0.05) + (pennies * 0.01), 2)
        if total_paid < price:
            print("Please add more coins, not enough! Start again, money returned.")
    change = round((total_paid - price), 2)
    print(f"You paid {total_paid}, you have {change} in change.")


run_the_coffee_machine()