#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("# # # # # # # # # # # # # # # # # # # #\n")
print("Welcome to the PyPassword Generator.")
print("\n# # # # # # # # # # # # # # # # # # # #\n")

nr_letters= int(input("Wie viele Buchstaben sollen in dem Passwort enthalten sein?\n")) 
nr_symbols = int(input(f"Wie viele Symbole?\n"))
nr_numbers = int(input(f"und wie viel Ziffern?\n"))

password = ""
#Eazy Level - Order not randomized:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# for char in range(1, nr_letters + 1):
#  randomChar = random.choice(letters)
#  password += randomChar

# for char in range(1, nr_symbols + 1):
#   randomChar = random.choice(symbols)
#   password += randomChar

# for number in range(1, nr_numbers + 1):
#   randomChar = random.choice(numbers)
#   password += randomChar

# print(password)
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
passwordList = []
for char in range(1, nr_letters + 1):
  passwordList.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
  passwordList.append(random.choice(symbols))

for number in range(1, nr_numbers + 1):
  passwordList.append(random.choice(numbers))

print(passwordList)
random.shuffle(passwordList)
for char in passwordList:
  password += char

print(f"Your Password is: {password}")