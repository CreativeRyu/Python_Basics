# # # # Lv 9 Script Dictionaries | Nested Dictionaries # # # #

"""___  _    _   _                   _
  |   \(_)__| |_(_)___ _ _  __ _ _ _(_)___ ___
  | |) | / _|  _| / _ \ ' \/ _` | '_| / -_|_-<
  |___/|_\__|\__|_\___/_||_\__,_|_| |_\___/__/
# # # # # # # # # # # # # # # # # # # # # # # #
"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

"""
+=============+
|   ToolBox   |
+=============+
"""

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Ein Dictionary besteht aus Key Value Pairs

# Key   : Value
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again"
    # Key 123 adden: random Text
}

# Items aus einem Dictionary abrufen
print(programming_dictionary["Bug"])

# Neue Items einem Dictionary hinzufügen
programming_dictionary["Testing"] = "Method to varify functional code."
print(programming_dictionary)

# Ein leeres Dictionary erzeugen
empty_dictionary = {}

# Ein vorhandenes Dictionary leeren -> Game Restart, Stats reset
# programming_dictionary = {}

# Ein Dictionary editieren -> Key Referenz und neuen String hinzufügen
programming_dictionary["Bug"] = "Eine Motte in deinem Rechner."

# Ein Dictionary durchiterieren
for key in programming_dictionary: # dahinter befindet sich die dictionary.keys() Funktion
    print(key)
    print(programming_dictionary[key])

    # - > Damit Key und Value wieder gemeinsam ausgegeben werden können
    # print(f"{key} : {programming_dictionary[key]}")

# in und not in
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
words = ['cat', 'lion', 'horse']

for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "is not in dictionary")

# ergänzend zur dictionary.keys() Function existiert die dictionary.values() Function
for french in dictionary.values():
    print(french)

# Insert neues Element in einem Dictionary
dictionary.update({"duck": "canard"})

# Ein Element aus einem Dictionary entfernen
# Ein Value wird nie ohne seinen Key im Dictionary erhalten bleiben
# Wird der Key entfernt, so wird also auch das zugehörige Value Pair entfernt
del dictionary["dog"]

# dictionary.items()
for key, value in dictionary.items():
    print("French/English ->", key, ":", value)

# copy a dictionary with dictionary.copy()

# create a dictionary out of a tuple
colors = (("green", "#008000"), ("blue", "#0000FF"))

colors_dictionary = dict(colors)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

"""
+=============+
|  Questline  |
+=============+
"""

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

"""
+================================+
|                                |
|  Lv 9 Quest 1 Grading Program  |
|                                |
+================================+
"""

# Sie haben Zugriff auf eine Datenbank mit student_scores im Format eines Dictionaries.
# Die Keys (Schlüssel) in student_scores sind die Namen der Studenten und die Values (Werte) sind ihre Prüfungsergebnisse.
# Schreiben Sie ein Programm, das die Punktzahlen in Noten umwandelt.
# Am Ende Ihres Programms sollten Sie ein neues Dictionary namens student_grades haben,
# das die Namen der Schüler als Keys und ihre Noten als Values enthält.
# Die endgültige Version des Dictionaries student_grades wird geprüft.

# Bedingungen: Ändern Sie NICHT das bestehende Dictionary student_scores und schreiben Sie KEINE print Anweisungen.

# Dies sind die Bewertungskriterien:

#     Punktzahl 91 - 100: Note = "Hervorragend"
#     Punktzahl 81 - 90: Note = "Übertrifft die Erwartungen".
#     Punktzahl 71 - 80: Note = "Akzeptabel".
#     Punktzahl 70 oder niedriger: Note = "Nicht bestanden"

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
    "Luna": 91
}
# 🚨 Don't change the code above 👆

# TODO-1: Erstellen Sie ein leeres Dictionary mit dem Namen student_grades.

# TODO-2: Schreiben Sie den Code, der die Noten dem student_grades Dictionary hinzufügt unter dieser Zeile.👇

# 🚨 Don't change the code below 👇
print(student_grades)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

"""_  _        _   _
  | \| |___ __| |_(_)_ _  __ _
  | .` / -_|_-<  _| | ' \/ _` |
  |_|\_\___/__/\__|_|_||_\__, |
# # # # # # # # # # # # # |___/
""" 


capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nesting a List in a Dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# Wert einer nested List aus dem Dictionary ausgeben
print(travel_log["France"][0])

# Ein Dictionary in einem Dictionary verschachteln
# Travel Log, zusätzlich möchte ich mit angeben wie oft ich bereits in dem Land gewesen bin
# als kleine Challenge -> Die Liste oben in ein Dictionary umwandeln und dabei als Key "cities_visited" nutzen
# anschließend "totals_visits" hinzufügen und die Zeile für Germany wiederholen
# total_visits beschreibt, wie oft das Land insgesamt besucht wurde 
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

# Nesting Dictionaries in Lists
# erst einmal alles als Dictionary und in einer Zeile
travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5,
    },
]

order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []}
}

print(order["main"][2][0])

# ---------------------------------------------------------------------

"""
+================================+
|                                |
| Lv 9 Quest 2 Dictionary in List|
|                                |
+================================+
"""

# Schreiben Sie ein Programm, das einen weiteren travel_log hinzufügen kann.
# Es ist bereits ein travel_log als Liste vorhanden, der zwei Dictionaries enthält.
# Schreiben Sie eine Funktion, die mit der unten aufgeführten Codezeile interagiert
# und den Eintrag für Russland zum travel_log hinzufügt.

# add_new_country("Russland", 2, ["Moskau", "Sankt Petersburg"])

#   Sie haben Russland 2 Mal besucht.
#   Du warst in Moskau und Sankt Petersburg.

# travel_log darf in diesem Zusammenhang NICHT direkt verändert werden.

# Hinweis
# Schauen Sie sich den Funktionsaufruf oben an, um zu sehen, wie der Name der Funktion lauten sollte.
# Die Eingaben für die Funktion sind positionsbezogene Argumente. Die Reihenfolge ist sehr wichtig.
# Sie können die Namen der Parameter frei wählen.

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]
# 🚨 Do NOT change the code above

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 👇


# 🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)