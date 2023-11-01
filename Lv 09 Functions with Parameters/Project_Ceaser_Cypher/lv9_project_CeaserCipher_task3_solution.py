alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def ceaser(base_text, shift_amount, cipher_direction):
  final_text = ""
  for letter in base_text:
    if letter == " ":
      final_text += " "
      
    else:  
      position = alphabet.index(letter)
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
        
  print(f"The {cipher_direction}d text is {final_text}")

ceaser(text, shift, direction)

#  TODO-1: Refaktorieren Sie die beiden Methoden, sodass am Ende nur noch eine Methode übrig bleibt.