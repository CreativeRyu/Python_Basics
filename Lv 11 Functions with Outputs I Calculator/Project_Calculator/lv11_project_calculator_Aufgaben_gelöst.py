# # # # # # # # # # # # # # # # #
# # Lv 10 Project Calculator # #
# # # # # # # # # # # # # # # # #

# 1. Erstellen Sie Funktionen für die vier mathematischen Standardrechenarten
# + - * /

# 2. Erstelle ein Dictionary, in das die Funktionen als Values eingesetzt werden. Die Symbole der Rechenarten werden als Keys verwendet.


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

num1 = int(input("Gib die erste Zahl ein: \n"))
# num2 = int(input("Gib die zweite Zahl ein: \n"))

# 3. Die Operatoren aus dem Dictionary sollen untereinander in der Konsole angezeigt werden.

for key in operations:
    print(key)

operation_symbol = input("Wat willste rechnen?")  # gegeben
num2 = int(input(
    "Gib die zweite Zahl ein: \n"))  # Place here for Better user experience
calculation = operations[operation_symbol]
first_result = calculation(num1, num2)

# 4. Erstellen Sie den Code der zur erfolgreichen Ausgabe der folgenden Zeile führt
print(f"{num1} {operation_symbol} {num2} = {first_result}")

# 5. Was ist wenn mit einer dritten Zahl weiter gerechnet wird?
operation_symbol = input("Willste weiter rechnen? Womit Brudi?")
num3 = int(input("Gib eine dritte Zahl ein: \n"))
calculation = operations[operation_symbol]
second_result = calculation(first_result, num3)

print(f"{first_result} {operation_symbol} {num3} = {second_result}")
