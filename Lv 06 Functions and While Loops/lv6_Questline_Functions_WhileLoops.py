# # # # Lv 6 Script Functions | While Loops # # # #
"""
   ___             _   _             
  | __|  _ _ _  __| |_(_)___ _ _  ___
  | _| || | ' \/ _|  _| / _ \ ' \(_-<
  |_| \_,_|_||_\__|\__|_\___/_||_/__/                
"""
# to Train with functions check
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json

print("Hello")
numChar = len("Hello")
print(numChar)

def myFunction():
  print("This is my first Python Function")

myFunction()

# Funktionen müssen vor ihrem Aufruf definiert werden
# Funktionen dürfen nicht den gleichen Namen wie eine Variable haben

#---------------------------------------------------------------------
"""
  __      ___    _ _       _                     
  \ \    / / |_ (_) |___  | |   ___  ___ _ __ ___
   \ \/\/ /| ' \| | / -_) | |__/ _ \/ _ \ '_ (_-<
    \_/\_/ |_||_|_|_\___| |____\___/\___/ .__/__/
                                        |_|
"""
# While Loops
something = True

while something == True:
 #Do something repeatedly
 print(something)

#---------------------------------------------------------------------
"""
+================================+
|                                |
|    Lv 6 Quest Loop 1 bis 10    |
|                                |
+================================+
"""
# Lösung
count = 0
while count < 10:
  print(count)
  count = count + 1

#---------------------------------------------------------------------
"""
+================================+
|                                |
|   Lv 6 Training Secret Number  |
|                                |
+================================+
"""

# Lösung
# number = 0

# while number != secret_number:
#   number = int(input("Type your integer Number here: "))
#   if number != secret_number:
#     print(20 * "# ")
#     print()
#     print("Ha ha! You're stuck in my loop!")
#     print()
#     print(20 * "# ")
#   else:
#     print(20 * "# ")
#     print()
#     print("Well done, muggle! You are free now.")
#     print()
#     print(20 * "# ")

#---------------------------------------------------------------------
"""
+================================+
|                                |
|       Continue | Break         |
|                                |
+================================+
"""

# Beispiel für break
print("The break instruction:")
for i in range(1, 7):
    if i == 4:
        break
    print("Inside the loop.", i)
print("Outside the loop.")


# Beispiel für continue
print("\nThe continue instruction:")
for i in range(1, 7):
    if i == 4:
        continue
    print("Inside the loop.", i)
print("Outside the loop.")

#---------------------------------------------------------------------

while True:
  print("Wir sind in der Schleife")
  eingabe = input("Soll die Schleife weiter laufen? | j für Ja und n für Nein")
  if eingabe == "n":
    break
  
print("# # # # ENDE DE SCHLEIFE # # # #")

#---------------------------------------------------------------------
"""
+================================+
|                                |
|     Lv 6 Training break        |
|                                |
+================================+
"""
# Die break-Anweisung wird zum Verlassen/Beenden einer Schleife verwendet.
# Entwerfen Sie ein Programm, das eine while-Schleife verwendet und den Benutzer fortlaufend auffordert, 
# ein Wort einzugeben, bis der Benutzer "chupacabra" als geheimes Ausstiegswort eingibt. 
# In diesem Fall sollte die Meldung "Sie haben die Schleife erfolgreich verlassen" 
# auf dem Bildschirm ausgegeben und die Schleife beendet werden.


# Lösung
# secret_word = "chupacabra"

# while True:
#   user_word = input("Geben Sie ein beliebiges Wort ein: ")
#   if user_word == secret_word:
#     break

# print("You've successfully left the loop.")

#---------------------------------------------------------------------
"""
+================================+
|                                |
|     Lv 6 Training continue     |
|                                |
+================================+
Die continue-Anweisung wird verwendet, 
um den aktuellen Block zu überspringen und zur nächsten Iteration überzugehen, 
ohne die Anweisungen innerhalb der Schleife auszuführen.
Sie kann sowohl mit der while- als auch mit der for-Schleife verwendet werden.
"""
# Schreiben Sie ein Programm, in dem Sie die folgenden Anforderungen umsetzen

#  + den Benutzenden auffordern, ein Wort einzugeben;
#  + user_word = user_word.upper() verwenden, 
#     um das vom Benutzenden eingegebene Wort in Großbuchstaben umzuwandeln; 
#  + verwenden Sie Bedingungen und die continue-Anweisung, 
#     um die folgenden Vokale A, E, I, O, U aus dem eingegebenen Wort zu verschwinden zu lassen
#  + geben Sie die übrig gebliebenen Buchstaben auf dem Bildschirm aus, 
#     und zwar jeden einzelnen in einer eigenen Zeile.

# ---- Start Code Snippet ---- #
# Prompt the user to enter a word
# and assign it to the user_word variable.

for letter in user_word:
    # Complete the body of the for loop.
    pass


# ---- Lösung ---- #
# user_word = input("Geben Sie ein Wort ein, aus dem die Vokale entfernt werden sollen: ")
# user_word = user_word.upper()

# for letter in user_word:
#     if letter == "A" or letter == "E" or letter == "I" or letter == "O" or letter == "U":
#       continue
#     print(letter)

# ---- Lösung mit Variable die befüllt werden soll ---- #
# user_word = input("Geben Sie ein Wort ein, aus dem die Vokale entfernt werden sollen: ")
# user_word = user_word.upper()
# word_without_vowels = ""

# for letter in user_word:
#     if letter == "A" or letter == "E" or letter == "I" or letter == "O" or letter == "U":
#       continue
#     word_without_vowels = word_without_vowels + letter
# print(word_without_vowels)

#---------------------------------------------------------------------
"""
+================================+
|                                |
|      Lv 6 while for else       |
|                                |
+================================+
"""

i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)
    
#---------------------------------------------------------------------

for i in range(5):
    print(i)
else:
    print("else:", i)

#--------------------------------------------------------------------- 
"""
+================================+
|                                |
|      Lv 6 Trainig Pyramide     |
|                                |
+================================+
"""
# Scenario: Ein Junge und sein Onkel, ein Computerprogrammierer, 
# spielen mit Holzbausteinen. Sie bauen eine Pyramide.
# Die Pyramide wird nach einem einfachen Prinzip gestapelt: 
# Jede untere Schicht enthält einen Baustein mehr als die darüber liegende.

# Deine Aufgabe ist es, ein Programm zu schreiben, das die Anzahl der Blöcke, 
# die die Baumeister haben, ausliest und die Höhe der Pyramide ausgibt, 
# die mit diesen Blöcken gebaut werden kann.

# Hinweis: Die Höhe wird durch die Anzahl der vollständig fertiggestellten Schichten gemessen
# wenn die Baumeister nicht genügend Blöcke haben und die nächste Schicht nicht fertigstellen können, 
# beenden sie ihre Arbeit sofort.

blocks = int(input("Enter the number of blocks: "))

#
# Write your code here.
#	

print("The height of the pyramid:", height)


# ---- Lösung ---- #
block_string = "+=+"


blocks = int(input("Enter the number of blocks: "))
layer = 0
blocks_inlayer = 1

while blocks_inlayer <= blocks:
    layer = layer + 1
    blocks -= blocks_inlayer
    blocks_inlayer = blocks_inlayer + 1
    print(f"{layer * block_string}")

print("The height of the pyramid: ", layer)

#--------------------------------------------------------------------- 
"""
+================================+
|                                |
|  Lv 6 Trainig Lothar Collatz   |
|                                |
+================================+
"""

# Nimm eine beliebige nicht-negative und nicht-nullte ganze Zahl und nenne sie c0;
# wenn sie gerade ist, ermittle ein neues c0 als c0 ÷ 2;
# wenn sie ungerade ist, wird ein neues c0 als 3 × c0 + 1 ausgewertet;

# Schreiben Sie ein Programm, das eine natürliche Zahl einliest und die obigen Schritte ausführt, 
# solange c0 ungleich 1 ist. Die Schritte, die nötig sind, um das Ziel zu erreichen, sollen gezählt werden. 
# Ihr Code sollte auch alle Zwischenwerte von c0 ausgeben.
# Hinweis: Der wichtigste Teil der Aufgabe besteht darin, wie man die Idee von Collatz in eine while-Schleife umsetzt, 
# das ist der Schlüssel zum Erfolg.


# ---- Lösung ---- #
from time import sleep


c0 = int(input("Irgendeine positive ganze Zahl: "))
steps = 0

while c0 != 1:
    if c0 % 2 == 0:
        c0 = c0 / 2
    elif c0 % 2 != 0:
        c0 = (c0 * 3) + 1
    steps = steps + 1
    print(c0) 
    sleep(0.5) 
print(f"Steps: {steps}")  