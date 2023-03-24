# # # # Lv 4 Random | Lists | Nested Lists # # # #

"""
+================================+
|                                |
|         Randomization          |
|                                |
+================================+
"""

# Randomization funktioniert nur wenn das Modul "random" importiert wird
# Was passiert beim importieren eines Moduls
# piModule in einer extra Datei anlegen
import random
import piModule

print("Here comes a random int")
randomInt = random.randint(1,10)
print(randomInt)
print("Here comes a 2nd random int")
randomInt = random.randint(1,10)
print(randomInt)
print(piModule.pi)
# erzeugt einen zufälligen float zwischen 0 und 1
print("float between 0 and 1")
randomFloat = random.random()
print(randomFloat)
print("float between 0 and 5")
floatFive = randomFloat * 5
print(floatFive)

#-----------------------------------------------------------------------------
"""
+================================+
|                                |
|     Lv 4 Quest 1 Flip Coin     |
|                                |
+================================+
"""

# Schreiben Sie bitte ein Programm, das zufällig zwischen Kopf oder Zahl entscheidet
# und das Ergebnis in der Konsole ausgibt. So als würde eine Münze geworfen werden.
# Hint: Remember to import the random module first. 🎲

# Schreiben Sie Ihren Programmcode bitte unter dieser Zeile 👇

#-----------------------------------------------------------------------------
"""
+================================+
|                                |
|  Lv 4 Quest 2 Names Roulette   |
|                                |
+================================+
"""

# Split string method erläutern
# Was kann alles mit der Split Function gemacht werden
# ohne Parameter | mit Parameter

# Sie werden ein Programm schreiben, das einen zufälligen Namen aus einer Liste von Namen auswählt. 
# Die ausgewählte Person muss die gesamte Rechnung für alle bezahlen.
# Wichtig: Sie dürfen die Funktion choice() nicht verwenden.
# names_string.split zerlegt die Zeichenkette names_string in einzelne Namen und stellt sie in eine Liste 
# mit dem Namen "names" zusammen. Damit dies funktioniert, 
# müssen Sie alle Namen als "names" gefolgt von einem Komma und einem Leerzeichen eingeben. z.B. name, name, name

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

#-----------------------------------------------------------------------------
"""
+================================+
|                                |
|             Lists              |
|                                |
+================================+
"""

# https://docs.python.org/3/
# https://docs.python.org/3/tutorial/datastructures.html
fruites = []
fruites = ["Apple","Cherry","Lemon","Melon"]

# Indexing
print(fruites[1])
print(fruites[-1])

# Länge einer Liste
# len nimmt den Namen einer Liste entgegen und gib die Anzahl der aktuell darin gespeicherten Elemente aus
print(len(fruites))
fruites[1] = "Sherry"
fruites.append("Dragonfruit")
print(fruites)
fruites.extend(["Oranges","Mango"])
print(fruites)
# Ein neues Element in die Liste integrieren
fruites.insert(1, "Pomegrenate")
print(fruites)
# Löschen eines Elementes aus einer Liste
del fruites[1]
print(len(fruites))
print(fruites)

# Elemente in einer Liste tauschen
variable_1 = 1
variable_2 = 2

variable_1, variable_2 = variable_2, variable_1

#-----------------------------------------------------------------------------
"""
+================================+
|                                |
|       Lv 4 Lists Training      |
|                                |
+================================+
"""

hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.
# Step 1: write a line of code that prompts the user
# to replace the middle number with an integer number entered by the user.
# Step 2: write a line of code that removes the last element from the list.
# Step 3: write a line of code that prints the length of the existing list.

print(hat_list)


# ----- Lösung ----- # 
hat_list = [1, 2, 3, 4, 5]

print(hat_list)
number = int(input("Tausche bitte die Ziffer in der Mitte der Liste mit einer beliebig ausgewählten Ziffer."))

hat_list[2] = number
del[hat_list[-1]]
print(len(hat_list))
print(hat_list)

# del = instruction auf die gesamte Liste, wird die Liste selber, 
# nicht den Inhalt der Liste löschen

#-----------------------------------------------------------------------------

# element in some_list
# element not in some_list
some_list = [1, 2, 3, 4, 5, 42]
print(7 in some_list)
print(7 not in some_list)
print(42 in some_list)
some_list.count(42) # <- Zählt wie oft ein Element in einer Liste vorkommt

# Beispiel
drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]
hits = 0

for number in bets:
    if number in drawn:
        hits += 1

print(hits)

#-----------------------------------------------------------------------------
"""
+================================+
|                                |
|   Lv 4 in | not in Training    |
|                                |
+================================+
"""

# Stellen Sie sich eine Liste vor - nicht sehr lang, nicht sehr kompliziert, 
# nur eine einfache Liste mit einigen ganzen Zahlen. 
# Einige dieser Zahlen können sich wiederholen, und das ist der entscheidende Hinweis. 
# Wir wollen keine Wiederholungen.

# Ihre Aufgabe ist es, ein Programm zu schreiben, das alle Zahlenwiederholungen aus der Liste entfernt. 
# Das Ziel ist es, eine Liste zu erhalten, in der alle Zahlen nur einmal vorkommen.

# Hinweis: Gehen Sie davon aus, dass die Ausgangsliste im Code fest codiert ist - 
# Sie müssen sie nicht über die Tastatur eingeben. 

# Tipp: Es ist empfohlen, eine neue Liste als vorübergehenden Arbeitsbereich zu erstellen 
# Sie müssen die Liste nicht lokal aktualisieren.

# ---- Code Snippet ---- #
some_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# Schreiben Sie hier Ihren Code
#
print("Liste mit einzigartigen Elementen.")
print(some_list)


# ----- Lösung ----- # 
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
unique_list = []

for number in my_list:
    if number not in unique_list:
        unique_list.append(number)

print(unique_list)
print(my_list)

#-----------------------------------------------------------------------------

# Slices  [Start:End-1] 

#  start is the index of the first element included in the slice;
#  end is the index of the first element not included in the slice.

some_list = [0, 1, 2, 3, 4, 42]
new_list = some_list[1:-1]
print(new_list)

#-----------------------------------------------------------------------------

list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2[0]
# Wie würde der Output aussehen
print(list_3)

#-----------------------------------------------------------------------------
"""
+================================+
|                                |
|         Nested Lists           |
|                                |
+================================+
"""

fruits = ["Strawberrys","Nectarines","Apples","Grapes","Peaches","Cherries","Pears"]
vegetables = ["Spinach","Kale","Tomatoes","Celery", "Potatoes"]

# Listen werden als Listen in eine neue Liste integriert
dirtyDozen =[fruits, vegetables]

print(dirtyDozen)
print(dirtyDozen[1][1])

#-----------------------------------------------------------------------------
"""
+================================+
|                                |
|   Lv 4 Quest 3 Treasure Map    |
|                                |
+================================+
"""



# You are going to write a program that will mark a spot with an X.
# In the starting code, you will find a variable called map.
# This map contains a nested list. When map is printed this is what the nested list looks like:
# [['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]
# This is a bit hard to work with. ->So on lines 112 and 122<-, we've used this line of code print(f"{row1}\n{row2}\n{row3}" to format the 3 lists to be printed as a 3 by 3 square, each on a new line. 
# Your job is to write a program that allows you to mark a square on the map using a two-digit system. 
# The first digit is the vertical location and the second digit is the horizontal location. 
# So an input of 23 should place an X at the position shown in OneNote

# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇


#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

#-----------------------------------------------------------------------------