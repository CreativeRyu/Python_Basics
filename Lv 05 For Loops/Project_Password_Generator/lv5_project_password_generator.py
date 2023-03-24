#   ___                              _    ___                       _           
#  | _ \__ _ _______ __ _____ _ _ __| |  / __|___ _ _  ___ _ _ __ _| |_ ___ _ _ 
#  |  _/ _` (_-<_-< V  V / _ \ '_/ _` | | (_ / -_) ' \/ -_) '_/ _` |  _/ _ \ '_|
#  |_| \__,_/__/__/\_/\_/\___/_| \__,_|  \___\___|_||_\___|_| \__,_|\__\___/_|  
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #                                                                            

# Password Generator

# Erstellen Sie ein Programm, das ein Passwort für sie generiert.
# Es soll dabei nach der Anzahl der Buchstaben,
# der Anzahl der Symbole
# und der Anzahl der Ziffern fragen, die in dem Passwort enthalten sein sollen.
# Das Programm wählt dann zufällig die entsprechenden Zeichen aus den zugehörigen Listen aus
# und kombiniert diese zu einem Passwort

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Schwierigkeitsgrad: Normal - Keine Zufällige Anordnung:
# -> 4 Buchstaben, 2 Symbole, 2 Ziffern = JduE&!91

# Schwierigkeitsgrad: Schwer - Zufällige Anordnung aller Zeichen:
# -> 4 Buchstaben, 2 Symbole, 2 Ziffern = g^2jk8&P