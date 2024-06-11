# Lv 3 Project Tip Calculator

# Begrüßung Ihres Programms
# Wie hoch ist die komplette Rechnung?
# Wie viel Trinkgeld wollen Sie geben?
# Auf wie viele Personen soll die Rechnung aufgeteilt werden?

# Wenn die Rechnung beispielsweise 150€ hoch war, auf 5 Personen
# aufgeteilt wird und dabei ein Trinkgeld von 10 % gegeben wird.
# Dann sollte jede Person (150.00 / 5) * 1,1 zahlen
# Runden Sie das Ergebnis auf zwei dezimal Kommastellen

print("# # # # # # # # # # # # # # # # # # # # # # # # # #\n")
print("        Willkommen beim Tip Calculator Sir          \n")
print("# # # # # # # # # # # # # # # # # # # # # # # # # #\n")
totalBill = float(input("Wie hoch ist die Rechnung?\n"))
tipPercent = float(input("Wie viel Prozent Trinkgeld möchten Sie geben?\n"))
people = int(input("Auf wie viele Personen soll die Rechnung aufgeteilt werden?\n"))

tip = (totalBill / 100) * tipPercent
bill_with_tip = totalBill + tip

result = round(bill_with_tip / people, 2)

print(f"Jede Person sollte {result} zahlen")
print(f"{result:.2f}")