# # # # Lv 5.5 Tuples and Sets # # # #

# Tupel verhalten sich ähnlich wie Listen, sind jedoch unveränderbar,
# nachdem Sie einmal erstellt worden sind.

ein_tupel = (1, 10, 42, 100, 1000)
auch_ein_tupel = ("one",)
auch_eins = "one", # ohne Komma würde eine Variable deklariert werden
# ein_tupel.append(43) -> würde also eine Fehlermeldung werfen

# Lesender Zugriff ist möglich
print(ein_tupel[0])
print(ein_tupel[-1])
print(ein_tupel[1:])
print(ein_tupel[:-2])

for elem in ein_tupel:
    print(elem)
    
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# Weitere Funktionen die mit einem Tupel möglich sind
my_tuple = (1, 10, 100)

t1 = my_tuple + (1000, 10000)
t2 = my_tuple * 3

print(len(t2))
print(t1)
print(t2)
print(10 in my_tuple)
print(-10 not in my_tuple)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

tup = 1, 2, 3, 
eine_liste = list(tup)
print(type(eine_liste))    # outputs: <class 'list'>

neues_tuple = tuple(eine_liste)