# # # # Lv 5 Script For Loops | Range # # # #
"""
   ___          _                     
  | __|__ _ _  | |   ___  ___ _ __ ___
  | _/ _ \ '_| | |__/ _ \/ _ \ '_ (_-<
  |_|\___/_|   |____\___/\___/ .__/__/
                             |_|      
"""
fruits = ["Apple","Peach","Lemon"]
for fruit in fruits:
  print(fruit)

# Addition der Zahlen einer Liste durch eine For Schleife
numberz = [10, 42, 33, 100, 16]
total = 0
for number in numberz:
  total = total + number
  print(total)
#---------------------------------------------------------------------
"""
+================================+
|                                |
|  Lv 5 Quest 1 Average Height   |
|                                |
+================================+
"""

# Bitte schreiben Sie ein Programm, das die durchschnittliche Körpergröße der Schüler aus einer Liste von Körpergrößen berechnet.
# z.B. student_heights = [180, 124, 165, 173, 189, 169, 146]
# Die durchschnittliche Körpergröße kann berechnet werden, indem alle Körpergrößen addiert und durch die Gesamtzahl der Körpergrößen geteilt werden.
# z.B. 180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146
# Es gibt insgesamt sieben Werte in student_heights. -> 1146 ÷ 7 = 163.71428571428572
# Runden Sie das Ergebnis auf die nächste ganze Zahl.
# Wichtig: Die sum() oder len() Funktion darf nicht in der Antwort verwendet werden.
# Versuchen Sie, deren Funktionalität mit dem, was Sie über for-Schleifen gelernt haben, nachzubilden.

# 🚨 Ändern Sie bitte nicht den Code unter dieser Zeile 👇
print("# # # # # # # # # # # # # # # # # # # # # # # #\n")

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
   
print("\n# # # # # # # # # # # # # # # # # # # # # # # #\n")
# 🚨 Ändern Sie bitte nicht den Code über dieser Zeile 👆

# Schreiben Sie Ihren Code unter dieser Zeile 👇
#---------------------------------------------------------------------
"""
+================================+
|                                |
|    Lv 5 Quest 2 High Score     |
|                                |
+================================+
"""
# Schreiben Sie ein Programm, das die höchste Punktzahl aus einer Liste von Punktzahlen errechnet.
# z.B. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
# Wichtig: Sie dürfen die Funktionen max und min nicht verwenden.
# Nutzen Sie für die Lösung der Aufgabe lediglich einen *for Loop*
# Beispiel Ausgabe: Die höchste Punktzahl in der Klasse ist: x

# 🚨 Ändern Sie bitte nicht den Code unter dieser Zeile 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Ändern Sie bitte nicht den Code über dieser Zeile 👆

# Schreiben Sie Ihren Code unter dieser Zeile 👇

#---------------------------------------------------------------------
"""
                           ____    ___             _   _          
   _ _ __ _ _ _  __ _ ___ / /\ \  | __|  _ _ _  __| |_(_)___ _ _  
  | '_/ _` | ' \/ _` / -_) |  | | | _| || | ' \/ _|  _| / _ \ ' \ 
  |_| \__,_|_||_\__, \___| |  | | |_| \_,_|_||_\__|\__|_\___/_||_|
                |___/     \_\/_/                                  
"""
# For Loop with Range
# auf range() Funktionen aus den beiden vorherigen Quests verweisen
for number in range(10):
    print(number)
# print 1 - 10 gibt nur 1 - 9 aus, man muss also immer einen drauf zählen
# da der zweite Parameter der Stopparameter ist
for number in range(1, 11):
    print(number)

# Hier wird die Größe der Schritte definiert
# Start | Stop | Step Parameters
for number in range(1, 11, 3):
    print(number)

result = 0
for number in range(1, 101):
  result += number

print(result)

#---------------------------------------------------------------------
"""
+================================+
|                                |
|  Lv 5 Training 1 Mississippi   |
|                                |
+================================+
"""
# Ihre Aufgabe ist hier ein Programm zu Schreiben, 
# das mit Hilfe einer for-Schleife bis fünf zählt und dabei das Wort "mississippi" ausgibt. 
# Nachdem das Programm bis fünf gezählt hat, soll es die abschließende Meldung 
# "Fertig oder nicht, ich komme" auf dem Bildschirm ausgeben.

# ---- Code Snippet ---- #
#import time

# Write a for loop that counts to five.
    # Body of the loop - print the loop iteration number and the word "Mississippi".
    # Body of the loop - use: time.sleep(1)

# Write a print function with the final message.

# ---- Lösung ---- #
# import time

# # Write a for loop that counts to five.
# for second in range(1,6):
#     print(f"{second}. Mississippi...")
#     time.sleep(1)


# print("Time's up, ready or not, here I come.")

#---------------------------------------------------------------------
"""
+================================+
|                                |
|  Lv 5 Quest 3 Adding Numbers   |
|                                |
+================================+
"""
# Bitte schreiben Sie ein Programm, das die Summe aller geraden Zahlen von 1 bis 100 berechnet. 
# Die erste gerade Zahl wäre also die 2 und die letzte die 100.
# d.h. 2 + 4 + 6 + 8 +10 ... + 98 + 100
# Wichtig: In der Konsolenausgabe sollte nur eine print-Anweisung stehen. 
# Sie sollte nur die Endsumme ausgeben und nicht jeden Schritt der Berechnung.
# Hinweis: Es gibt mehrere Möglichkeiten, dieses Problem zu lösen, aber Sie müssen in jeder Lösung die Funktion range() verwenden.

# Zusatzaufgaben
# Lassen Sie ein weiteres Programm nur die ungeraden Zahlen und ein drittes Programm alle Zahlen von 1 bis 100 addieren.

# Schreiben Sie Ihren Code unter dieser Zeile 👇

#---------------------------------------------------------------------
"""
+================================+
|                                |
|     Lv 5 Quest 4 FizzBuzz      |
|                                |
+================================+
"""
# Schreiben Sie ein Programm, dass die Zahlen 1 bis 100 in der Konsole ausgibt
# Aber
# für jede Zahl die durch 3 teilbar ist, soll Fizz ausgegeben werden
# für jede Zahl die durch 5 teilbar ist, soll Buzz ausgegeben werden
# und für jede Zahl die durch 3 und durch 5 teilbar ist, soll FizzBuzz ausgegeben werden

# Schreiben Sie Ihren Code unter dieser Zeile 👇

#-----------------------------------------------------------------------------

"""
+================================+
|                                |
|    Lv 4 Training BubbleSort    |
|                                |
+================================+
"""

# # # # Bubble Sort Algorithm # # Sortieralgorithmus Bubblesort # # # #
numbers_list = [-2, 5, 47, 38, 3, 10, 112, 75, 81, 42, 43]

for number in range(numbers_list):
  print(number)


def bubblesort(list):
    for number in list:
        for i in range(0, len(list)-1):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                
                  # STRG + D
                  # STRG + K + C
                  # STRG + K + U

#--------------------------------------

def bubble_sort(our_list):
    # We go through the list as many times as there are elements
    for i in range(len(our_list)):
        # We want the last pair of adjacent elements to be (n-2, n-1)
        for j in range(len(our_list) - 1):
            if our_list[j] > our_list[j+1]:
                # Swap
                our_list[j], our_list[j+1] = our_list[j+1], our_list[j]

#--------------------------------------

def bubbleSort(array):
    
  # Forschleife um jedes Element im Array zu durchlaufen
  for num_of_iterations in range(len(array)):

    # Forschleife um die Elemente im Array zu vergleichen
    for j in range(0, len(array) - num_of_iterations - 1):

      # Vergleich zweier benachbarter Elemente
      # Wechsel von > zu < um in die aufsteigende Reihenfolge zu sortieren
      if array[j] > array[j + 1]:

        # Tauschen der Elemente, wenn diese
        # nicht in der korrekten Reihenfolge sind
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp

# print("\nAusgangsarray")

# print(numbers_array)

# bubblesort(numbers_array)

# print("\nSortierter Array")
# print(numbers_array)

#--------------------------------------

my_list = [8, 10, 6, 2, 4]  # list to sort
swapped = True  # It's a little fake, we need it to enter the while loop.

while swapped:
    swapped = False  # no swaps so far
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True  # a swap occurred!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(my_list)

# Sortierfunktion -> my_list.sort()
# Liste umdrehen -> my_list.reverse()

#-----------------------------------------------------------------------------