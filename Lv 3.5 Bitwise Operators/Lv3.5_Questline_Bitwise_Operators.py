x = 4  # 0000 0100
y = 1  # 0000 0001

a = x & 1
# 0000 0100 * 0000 0001 = 0
b = x | y
# 0000 0100 + 0000 0001 = 0000 0101 -> 5
c = ~x
# 0000 0100 negiert = 1011 -> 10 | Dezimalzahl + 1 und dann ein Minuszeichen ran -5 # 0101
# 2er Komplimentäre und das erste Bit als Sign für Negative Values
# https://www.youtube.com/watch?v=4qH4unVtJkE
# Das Sign Bit ist eine negative 8 | Beispiel 1010 => -8 + 2 = -6
# 1000 = -8
# 1001 = -7
# 1010 = -6
# 1011 = -5
# 1100 = -4
# 1101 = -3
# 1110 = -2
# 1111 = -1
# 0000 = 0
# 0001 = 1
# 0010 = 2
# 0011 = 3
# 0100 = 4
# 0101 = 5
# 0110 = 6
# 0111 = 7
# um also die Aufgabe zu lösen erst alle einer Komplementäre bilden also alle Bits invertieren
# aus 0101(5) also 1010 
# anschließend + 1 
# 1011 => -8 + 1 + 2 = -5
#  0100 1011 +1 => 1100 

d = x ^ 5
# 0000 0100 xor 0000 0101 = 0000 0001 -> 1
e = x >> 2
# 0000 0100 um 2 bit >> = 0000 0001 -> 1
f = x << 2
# 0000 0100 um 2 bit << = 0001 0000 -> 16

print(a, b, c, d, e, f)