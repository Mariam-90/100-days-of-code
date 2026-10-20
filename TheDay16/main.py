from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
maker = CoffeeMaker()
money = MoneyMachine()
print(menu.get_items())

drink = menu.find_drink("cappuccino")
print(drink.cost)
print(drink.name)
print(maker.report())
print(maker.resources)
print(maker.make_coffee(drink))

