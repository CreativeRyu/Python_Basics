# # # # Lv 14 Tic Tac Toe Game # # # #

"""
+================================+
|                                |
|Lv 14 Tic Tac Toe Game Scenario |
|                                |
+================================+
"""

# Ihre Aufgabe ist es, ein einfaches Programm zu schreiben, das so tut, als würde es mit dem Benutzer Tic-Tac-Toe spielen. 
# Um es Ihnen leichter zu machen, haben wir beschlossen, das Spiel zu vereinfachen. 

#     Der Computer (d.h. Ihr Programm) soll das Spiel mit "X" spielen;
#     der Benutzer (z.B. Sie) sollte das Spiel mit 'O's' spielen;
#     Der erste Zug gehört dem Computer - er setzt sein erstes "X" immer in die Mitte des Brettes;
#     alle Felder sind zeilenweise nummeriert, beginnend mit 1 (siehe die Beispielsitzung unten)
#     der Benutzer gibt seinen Zug ein, indem er die Nummer des von ihm gewählten Feldes eingibt - die Nummer muss gültig sein, 
#     d.h. sie muss eine ganze Zahl sein, sie muss größer als 0 und kleiner als 10 sein, 
#     und sie darf nicht auf ein Feld zeigen, das bereits besetzt ist;
#     das Programm prüft, ob das Spiel zu Ende ist - es gibt vier mögliche Fälle: 
#     1. das Spiel sollte fortgesetzt werden, 
#     2. das Spiel endet mit einem Unentschieden, 
#     3. Sie gewinnen, 
#     4. oder der Computer gewinnt;
#     der Computer antwortet mit seinem Zug und die Prüfung wird wiederholt;
#     keine künstliche Intelligenz einsetzen - eine zufällige Feldauswahl durch den Computer ist gut genug für das Spiel.

# Die Beispielsitzung mit dem Programm könnte wie folgt aussehen:

"""
+-------+-------+-------+
|       |       |       |
|   1   |   2   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+
Enter your move: 1
+-------+-------+-------+
|       |       |       |
|   O   |   2   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+
Enter your move: 8
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   O   |   9   |
|       |       |       |
+-------+-------+-------+
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   O   |   9   |
|       |       |       |
+-------+-------+-------+
Enter your move: 4
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   O   |   9   |
|       |       |       |
+-------+-------+-------+
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   O   |   9   |
|       |       |       |
+-------+-------+-------+
Enter your move: 7
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   O   |   O   |   9   |
|       |       |       |
+-------+-------+-------+
You won!
    
"""

# Anforderungen

# Implementieren Sie die folgenden Eigenschaften:

# Das Brett sollte als eine Liste mit drei Elementen gespeichert werden, 
# wobei jedes Element eine weitere Liste mit drei Elementen ist (die inneren Listen stellen Zeilen dar), 
# so dass auf alle Quadrate mit der folgenden Syntax zugegriffen werden kann:

# board[row][column]


# jedes Element der inneren Liste kann ein "O", 
# ein "X" oder eine Ziffer für die Nummer des Feldes enthalten (ein solches Feld wird als frei betrachtet)
# das Aussehen der Tafel sollte genau so sein wie im Beispiel dargestellt.
# implementieren Sie die Funktionen die bereits unten deklariert wurden


# Um eine zufällige ganze Zahl zu zeichnen, kann man eine Python-Funktion namens randrange() verwenden. 
# Das folgende Beispielprogramm zeigt, wie man sie benutzt (das Programm druckt zehn Zufallszahlen von 0 bis 8).

# Hinweis: Die Anweisung from-import ermöglicht den Zugriff auf die Funktion randrange, 
# die in einem externen Python-Modul mit dem Namen random definiert ist.
# from random import randrange

# for i in Bereich(10):
#     print(randrange(8))

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game


def draw_move(board):
    # The function draws the computer's move and updates the board.