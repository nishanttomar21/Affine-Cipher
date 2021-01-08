# Keys to encrypt and decrypt the message
key1 = 17
key2 = 20


# To take plain-text input from the user (Message to be encrypted)
def take_input():
    message = input("Enter your message to be encrypted (Use capital letters): ")
    return message.upper()                                                                # Making text input to small case


# To encrypt the message
def encryption(message):
    encrypted_message = ""

    for character in message:
        # Avoid space to be encrypted
        if character != " ":
          encrypted_message += chr(int((ord(character) - ord("A")) * key1 + key2) % 26 + ord("A"))      # Ord() function gives back ascii value
        # If space then directly add it to the encrypted message
        else:
          encrypted_message += character

    return encrypted_message


# So that this function doesn't run when some other file imports this file
if __name__ == "__main__":
    plain_text = take_input()
    encrypted_message = encryption(plain_text)

