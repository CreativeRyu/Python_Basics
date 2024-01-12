#1. Erstellen Sie eine Begrüßung für Ihr Programm
print("Welcome to the Band Name Generator.")
#2. Fragen Sie den Benutzenden, in welcher Stadt er oder sie aufgewachsen ist.
city = input("Where did you grow up in which City?\n")
#3. Fragen Sie den Benutzenden, nach seinem oder ihrem Lieblingstier.
animal = input("What is your favorite Animal?\n")
#4. Kombinieren Sie den Namen der Stadt, sowie den Namen des Lieblingstieres zu einem Band Namen.
result = (f"{city} {animal}s")
result = result.upper()
print("So your Band Name can be something like " + result + ".\n")
#5. Achten Sie darauf, dass der Curser anschließend in eine neue Zeile springt.
input()