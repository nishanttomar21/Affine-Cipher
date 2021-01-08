###########################################
# Affine Cipher using python
# Nishant Tomar
# 2020PMD4210
###########################################

# Keys to encrypt and decrypt the message
key1 = 17
key2 = 20


# To take plain-text input from the user (Message to be encrypted)
def take_input():
    print("\n\n#####################################")
    print("\t\t\tAFFINE CIPHER")
    print("#####################################\n\n")
    message = input("Enter your message to be encrypted (use capital letters and don't enter special characters): ")
    return message.upper()  # Making text input to small case


# To encrypt the message
def encryption(message):
    encrypted_message = ""

    # Loop till message length
    for character in message:
        # Avoid space to be encrypted
        if character != " ":
            encrypted_message += chr(                                                       # C = [(P*k1) + k2]mod26
                int((ord(character) - ord("A")) * key1 + key2) % 26 + ord("A"))             # ord() function gets ascii value and chr() gets character value of ascii

        # If space then directly add it to the encrypted message
        else:
            encrypted_message += character

    print("\n\nEncrypted Message: " + encrypted_message + "\n")

    return encrypted_message


# Calculating multiplicative inverse of integer modulo n --> [(key1*x)mod26=1]
def key_inverse():
    inverse = ""

    # Loop from 0 -> 26
    for i in range(0, 26):
        flag = int((key1 * i) % 26)

        # If multiplication inverse found
        if flag == 1:
            inverse = i

    return inverse


# To decrypt the encrypted message
def decryption(message):
    decrypted_message = ""

    key_inverse_value = key_inverse()                                                                   # Calculating inverse of key1

    # Loop till message length
    for character in message:
        # If character is not space
        if character != " ":
            decrypted_message += chr(
                int((((ord(character) - ord("A")) - key2) * key_inverse_value) % 26 + ord("A")))        # P = [(C-k2)*k1^-1]mod26

        # If character is space
        else:
            decrypted_message += character

    print("Decrypted Message: " + decrypted_message + "\n")

    return decrypted_message


# So that this function doesn't run when some other file imports this file
if __name__ == "__main__":
    plain_text = take_input()
    encrypted_message = encryption(plain_text)
    decryption(encrypted_message)
