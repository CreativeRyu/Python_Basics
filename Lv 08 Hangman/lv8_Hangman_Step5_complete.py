import random
from lv8_Hangman_Step5_Art import stages, logo
from lv8_Hangman_Step5_WordList import word_list

end_of_game = False

# Step 1 TODO 1
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Step 4 TODO 1
lives = 6
# ------------------------------------------------------
# word_list_length = len(word_list)-1
# chosen_word = random.randint(0,word_list_length)
# ------------------------------------------------------

# Step 2 TODO 1
display = []
for i in range(word_length):
  display.append("_")
# ------------------------------------------------------
print(f"{logo}\n")

# print(f'debug: {chosen_word}')
print(f"{' '.join(display)}")

# Step 3 TODO 1o
while not end_of_game:
  
# Step 1 TODO 2
  guess = input("\nWelcher Buchstabe könnte in diesem Wort enthalten sein?\n").lower()

# Step 1 TODO 3 Step 2 TODO 2
  for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter
      
# Step 4 TODO 2
  if guess not in chosen_word:
    lives -= 1
    print(f"Du hast {guess} geraten, dieser Buchstabe ist nicht im Wort enthalten, du verlierst ein Leben.")
    if lives == 0:
      end_of_game = True
      print("Du hast verloren.")

# Step 4 TODO 3
  print(stages[lives])
# Step 2 TODO 3
  print(f"{' '.join(display)}")

  # Step 3 TODO 1
  if "_" not in display:
    end_of_game = True
    print("\nDu hast gewonnen ;)")