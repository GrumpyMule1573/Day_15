from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_it_on = True
drink_options = Menu()
coffee_machine = CoffeeMaker()
money_taken = MoneyMachine()

while is_it_on:
    drink_choice = input(f"Which drink would you like? {drink_options.get_items()}: ").lower()
    # drink_ordered returns a MenuItem() object
    drink_ordered = drink_options.find_drink(drink_choice)
    if drink_choice == "report":
        coffee_machine.report()
    elif drink_choice == "off":
        is_it_on = False
    elif drink_ordered is not None:
        print(drink_ordered.ingredients)
        if coffee_machine.is_resource_sufficient(drink_ordered):
            coffee_machine.make_coffee(drink_ordered)
            print("drink made")
            money_taken.make_payment(drink_ordered.cost)
