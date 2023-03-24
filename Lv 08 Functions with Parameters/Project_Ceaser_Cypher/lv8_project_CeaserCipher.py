import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
should_continue = True
print(art.logo)

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
          new_position = 26 + new_position
          
      new_letter = alphabet[new_position]
      final_text += new_letter  
    else: 
      final_text += char
  print(f"The {cipher_direction}d text is {final_text}")

#-------------------------------------------------------------------

while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  caesar_cipher(text, shift, direction)
  result = input("Type 'Yes' if you want to go again. Otherwise type 'no'. \n")
  if result == "no":
    should_continue = False
    print("See ya next time Dude 😏👉")