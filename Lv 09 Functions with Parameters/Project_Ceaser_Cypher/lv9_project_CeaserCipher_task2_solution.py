alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(message_text, shift_amount):
  cipher_text = ""
  for letter in message_text:
    if letter == " ":
        cipher_text += " "
    else:
      position = alphabet.index(letter)
      new_position = position + shift_amount
      if new_position > 25:
        new_position = new_position - 26
      new_letter = alphabet[new_position]
      cipher_text += new_letter
  print(f"The encoded text is {cipher_text}")

def decrypt(cipher_text, shift_amount):
  real_text = ""
  for letter in cipher_text:
    if letter == " ":
      real_text += " "
    else:
      position = alphabet.index(letter)
      new_position = position - shift_amount
      if new_position < 0:
        new_position = 26 - new_position
    new_letter = alphabet[new_position]
    real_text += new_letter
  print(f"The decoded text is {real_text}")

if direction == "encode":   
  encrypt(text, shift)
if direction == "decode":   
  decrypt(text, shift)

# TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

# TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"

#  TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.