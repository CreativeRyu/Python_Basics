# # # # # # # # # # # # # # # # #
# # Lv 10 Project Calculator # #
# # # # # # # # # # # # # # # # #

from replit import clear
from art import logo


# Add
def add(n1, n2):
    return n1 + n2


# Substract
def substract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


#Divide
def divide(n1, n2):
    return n1 / n2


operations = {"+": add, "-": substract, "*": multiply, "/": divide}


def calculator():
    print(logo)
    should_continue = True
    num1 = float(input("Gib die erste Zahl ein: \n"))

    for key in operations:
        print(key)

    while should_continue:
        operation_symbol = input("Wat willste rechnen?\n")
        num2 = float(input("Wie lautet die nächste Zahl: \n"))
        calculation = operations[operation_symbol]
        result = calculation(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {result}")

        continue_string = input(
            f"Willste mit {result} weiter rechnen? 'y' für Ja ich will oder 'n' für ne du lass ma. \n"
        )
        continue_string = continue_string.lower()
        if continue_string == "y":
            num1 = result
        if continue_string == "n":
            should_continue = False
            clear()
            calculator()

calculator()
