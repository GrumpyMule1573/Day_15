from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_it_on = True
drink_options = Menu()
coffee_machine = CoffeeMaker()
money_taken = MoneyMachine()

while is_it_on:
    drink_choice = input(f"Which drink would you like? {drink_options.get_items()}: ").lower()
    # drink_ordered is a MenuItem() object from drink_options.find_drink(drink_choice)
    drink_ordered = drink_options.find_drink(drink_choice)
    if drink_choice == "report":
        coffee_machine.report()
        money_taken.report()
    elif drink_choice == "off":
        is_it_on = False
    elif drink_ordered is not None:
        if coffee_machine.is_resource_sufficient(drink_ordered):
            if money_taken.make_payment(drink_ordered.cost):
                coffee_machine.make_coffee(drink_ordered)

