alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def change(text, shift_amount):
  end_text = ""
  if direction=="decode":
    shift_amount=-1*shift_amount;
    cipher="decoded"
  else:
    cipher="encoded"
    
  for char in text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text+=char
      
  print(f"The {cipher} text is {end_text}")
flag=1
while flag==1:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift%=26
  change(text,shift)
  result=input("Type 'yes'to continue and 'no' to exit\n")
  if result=="yes":
    flag=1
  else:
    flag=0
            
