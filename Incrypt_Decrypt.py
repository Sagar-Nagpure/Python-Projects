alphabate = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',]

def encryption(plain_text,shift_key):
 cipher_text = ""
 for char in plain_text:
    if char in alphabate:
        position = alphabate.index(char)
        new_position = (position + shift_key) % 26
        cipher_text += alphabate[new_position]
    else:
       cipher_text += char
 print(f"Your encrypted message is: {cipher_text}")

def decryption(cipher_text,shift_key):
 plain_text = ""
 for char in cipher_text:
    if char in alphabate:
        position = alphabate.index(char)
        new_position = (position - shift_key) % 26
        plain_text += alphabate[new_position]
    else:
       plain_text += char
 print(f"Your decrypted message is: {plain_text}")

wanna_end = False

while not wanna_end:
    what_to_do = input("Type 'encrypt' for encryption, type 'decrypt' for decryption:\n")
    text = input('Type your message :\n')
    shift = int(input('Enter shift key:\n'))
    if what_to_do == 'encrypt':
        encryption(plain_text = text, shift_key = shift)
    elif what_to_do == 'decrypt':
        decryption(cipher_text = text, shift_key = shift)

    play_again = input("Type 'Yes' to continue or Type 'No' to end: ")

    if play_again == 'No' or 'no':
     wanna_end == True
  
print("Have a nice day !")
