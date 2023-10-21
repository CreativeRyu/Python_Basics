import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
should_continue = True
print(art.logo)

#     #TODO-3: What happens if the user enters a number/symbol/space?
#     #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?

def caesar_cipher(base_text, shift_amount, cipher_direction):
  final_text = ""
  for char in base_text:
    if char in alphabet:
      
      position = alphabet.index(char)
      if cipher_direction == "encode":
        new_position = position + shift_amount
        if new_position > 25:
          new_position = new_position - 26          
        
      elif cipher_direction == "decode":
        new_position = position - shift_amount
        if new_position < 0:
          new_position = 26 - new_position
          
      new_letter = alphabet[new_position]
      final_text += new_letter  
    else: 
      final_text += char
  print(f"The {cipher_direction}d text is {final_text}")

#TODO-1: Import and print the logo from art.py when the program starts.

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 

while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

#TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#Try running the program and entering a shift number of 45.
#Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
#Hint: Think about how you can use the modulus (%).

  caesar_cipher(text, shift, direction)
  result = input("Type 'Yes' if you want to go again. Otherwise type 'no'. \n")
  if result == "no":
    should_continue = False
    print("See ya next time Dude 😏👉")