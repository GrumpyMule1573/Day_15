from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_it_on = True

while is_it_on:
    drink_options = Menu()
    coffee_machine = CoffeeMaker()
    drink_choice = input(f"Which drink would you like? {drink_options.get_items()}: ").lower()
    drink_ordered = drink_options.find_drink(drink_choice)
    if drink_choice == "report":
        coffee_machine.report()
    elif drink_choice == "off":
        is_it_on = False
    elif drink_ordered is None:
        print(drink_ordered.name)
    is_it_on = False
