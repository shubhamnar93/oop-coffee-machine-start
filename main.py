from platform import machine
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu=Menu()
money = MoneyMachine()
cofee_maker=CoffeeMaker()
is_turn=True
while is_turn:
    names=menu.get_items()
    cofee=input(f"amoung the {names} which cofee you want to drink: ")
    if cofee =='off' or cofee=='no':
        is_turn=False
    elif cofee=='report':
        cofee_maker.report()
        money.report()
    else:
        coffee= menu.find_drink(cofee)
        cost = coffee.cost
        if cofee_maker.is_resource_sufficient(coffee):
            if money.make_payment(cost):
                cofee_maker.make_coffee(coffee)
    


