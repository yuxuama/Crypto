#Author: Yuxuama
##  Encoding a message with Cesar process  ##

def cesar_encrypt():
    key = int(input("Donne une clé de codage: "))
    if not 0 < key < 26:                                                              #Check if is in the range for a Cesar encode
        raise ValueError("La clé de codage doit être comprise entre 0 et 26")
    message = input("Donne le message que tu veux crypter: ")
    crypted_message = ''
    for char in message:
        ord_char = ord(char)
        if ord_char != 32 or ord_char != 44:                                          #I have a problem here the 'or' simply doesn't work and I don't know why
            crypted_message = crypted_message + chr((ord_char - 97 + key) % 26 + 97)  #Coding char, the method allows to be only in the alphabet
        else:
            crypted_message = crypted_message + char
    return crypted_message

## Computation of all solution for a given coded chain ##

def cesar_bf(chain):
    decrypted_message = ''
    for i in range(-25, 1):
        for char in chain:
            if char != ' ':
                decrypted_message = decrypted_message + chr((ord(char) + i -97) % 26 + 97)
            else:
                decrypted_message = decrypted_message + char
        print(decrypted_message, "the key was: ", -i)
        decrypted_message = ''

message = cesar_encrypt()
print(" ")
print("######  Encoded message   ######")
print(message)
print("################################ ")
print(" ")
print("######  Decoded solution  ######")
cesar_bf(message)
print("################################")