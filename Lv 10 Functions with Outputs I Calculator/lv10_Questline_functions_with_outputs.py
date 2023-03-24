# # # # Lv 10 Functions with Outputs | Rekursion # # # #
"""      _
 _ _ ___| |_ _  _ _ _ _ _
| '_/ -_)  _| || | '_| ' \
|_| \___|\__|\_,_|_| |_||_|
"""

def fill_hearts(hearts = 0):
    if hearts == 0:
        return
    else:
        print(f"Got filled up your hearts by {hearts}.")

fill_hearts()
fill_hearts(2)

def format_name(f_name, l_name):
    f_name = f_name.title()
    l_name = l_name.title()
    # print(f"{f_name} {l_name}")
    return f"{f_name} {l_name}"

# formated_string = format_name("ryu", "rONin")
print(format_name("ryu", "rONin"))

output = len("Ryu")

# Multi return in Tupel oder einzelne Variablen
def spam():
    wert = 42
    return wert * 2, wert / 2, "Auch ich werde zurückgegeben"


# Zurückgegebenes Tupel wird in den entsprechenden Variablen gespeichert
great_value, small_value, some_text = spam()
print(great_value)
print(small_value)
print(some_text)

# print(type(great_value))
# print(type(small_value))
# print(type(some_text))

# Das gesamte Tupel wird in einer Variable vom Typ Tupel gespeichert
one_variable = spam()
print(type(one_variable))

####################################################################################

"""
+================================+
|                                |
|  Lv 10 Quest 1 Days in Month   |
|                                |
+================================+
"""

# Im bereits vorhandenen Code finden Sie die Lösung der Schaltjahr-Aufgabe. 
# Zunächst wandeln Sie die Funktion is_leap() so um, 
# dass sie statt "Schaltjahr." oder "Nicht Schaltjahr." True zurückgibt, 
# wenn es sich um ein Schaltjahr handelt und False, wenn es kein Schaltjahr ist.

# Bitte erstellen Sie anschließend eine Funktion mit dem Namen days_in_month(),
# die das Jahr und einen Monat als Eingaben benötigt, z.B.
# days_in_month(Jahr=2022, Monat=2)

# Anhand dieser Informationen berechnet die Funktion 
# die Anzahl der Tage im Monat und gibt diese dann als Ausgabe zurück, z. B:
# 28

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Leap year.")
            else:
                print("Not leap year.")
        else:
            print("Leap year.")
    else:
        print("Not leap year.")


def days_in_month():
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


# 🚨 Bitte verändern Sie nichts an unten aufgeführten Codezeilen
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

####################################################################################

"""
 ___     _               _          
| _ \___| |___  _ _ _ __(_)___ _ _  
|   / -_) / / || | '_(_-< / _ \ ' \ 
|_|_\___|_\_\\_,_|_| /__/_\___/_||_|
"""

def twist_numbers(number):
    if number > 7:
        number = number - 1
        number = twist_numbers(number)
        return number
    return number


####################################################################################

"""
 _                 _          ___ _     _          _ 
| |   ___  __ __ _| | __ __  / __| |___| |__  __ _| |
| |__/ _ \/ _/ _` | | \ \ / | (_ | / _ \ '_ \/ _` | |
|____\___/\__\__,_|_| /_\_\  \___|_\___/_.__/\__,_|_|
"""

# Beispiel 1
def spam_global():
    print(eggs)
eggs = 10 # globale Variablen Definition

spam_global()

################################

# Beispiel 2
def spam_local():
    print(eggs)
    eggs = 42
eggs = 10

spam_local()

################################

def spam_chaos():
    global eggs
    eggs = 43

####################################################################################

"""
+================================+
|                                |
|   Lv 10 Training Date of Day   |
|                                |
+================================+
"""
# Ihre Aufgabe ist es, eine Funktion zu schreiben und zu testen, 
# die drei Argumente annimmt (ein Jahr, einen Monat und einen Tag des Monats) und den entsprechenden Tag des Jahres zurückgibt, 
# oder keine zurückgibt, wenn eines der Argumente ungültig ist.

# Verwenden Sie die zuvor geschriebenen und getesteten Funktionen. 

# def is_year_leap(year):
# #
# # Your code from leap Year
# #

# def days_in_month(year, month):
# #
# # Your code from days in month
# #

# def day_of_year(year, month, day):
# #
# # Your new Code
# #  

# print(day_of_year(2000, 12, 31))

####################################################################################
# Collected by Creative Djinn Ryu Ronin