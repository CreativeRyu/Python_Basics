rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

paper = ''' 
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

#Write your code below this line 👇
import random

print("Hi there, we play a round of the most epic Game out there \nROCK PAPER SCISSORS.")
print("The Computer Enemy is badass but you're still able to beat him, so what is your choice?")
playersChoice = int(input("1 for Rock, 2 for Paper, or 3 for Scissors?\n"))
randomChoice = random.randint(1,3)
gameImages = [rock, paper, scissors]

# Players Choice
if playersChoice > 3 or playersChoice < 1:
  print("You typed an invalid Number. I said 1, 2 or 3. There are Rules in this World and we all have to follow them.")

if playersChoice == 1:
  print("You:")
  print(gameImages[playersChoice-1])
elif playersChoice == 2:
  print("You:")
  print(gameImages[playersChoice-1])
elif playersChoice == 3:
  print("You:")
  print(gameImages[playersChoice-1])

# Computers Choice
if randomChoice == 1:
  print("Computer:")
  print(gameImages[randomChoice-1]) 
elif randomChoice == 2:
  print("Computer:")
  print(gameImages[randomChoice-1])
elif randomChoice == 3:
  print("Computer:")
  print(gameImages[randomChoice-1])

# Results
if randomChoice == playersChoice:
  print("DRAW")

elif playersChoice == 1 and randomChoice == 2 or playersChoice == 2 and randomChoice == 3 or playersChoice == 3 and randomChoice == 1:
  print("Damn you lose Man.")

elif playersChoice == 1 and randomChoice == 3 or playersChoice == 2 and randomChoice == 1 or playersChoice == 3 and randomChoice == 2:
  print("!! YOU WIN !!")