#Author: Yuxuama

#declaration of dedicated alphabet

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_char = "!?:;.,'éèàçù"
numbers = "0123456789"


##  Encoding a message with Cesar process  ##

def cesar_encrypt():

    # Asking for key
    key = int(input("Donne une clé de codage: "))
    if not 0 < key < 26:      #Check if the key is in the range for a Cesar encode
        raise ValueError("La clé de codage doit être comprise entre 0 et 26")

    #Asking for message
    message = input("Donne le message que tu veux crypter: ")
    crypted_message = ''

    #Crypt th message
    for char in message:
        if char in lowercase:
            new_index = (lowercase.index(char) + key) % 26
            crypted_message += lowercase[new_index]
        elif char in uppercase:
            new_index = (uppercase.index(char) + key) % 26
            crypted_message += uppercase[new_index]
        elif char in special_char:
            new_index = (special_char.index(char) + key) % 12
            crypted_message += special_char[new_index]
        elif char in numbers:
            new_index = (numbers.index(char) + key) % 10
            crypted_message += numbers[new_index]
        else:
            crypted_message += char
    return crypted_message

## Computation of all solution for a given coded chain ##

def cesar_bf(chain):
    decrypted_message = ''
    for i in range(26):
        for char in chain:
            if char in lowercase:
                new_indew = (lowercase.index(char) - i) % 26
                decrypted_message += lowercase[new_indew]
            elif char in uppercase:
                new_indew = (uppercase.index(char) - i) % 26
                decrypted_message += uppercase[new_indew]
            elif char in special_char:
                new_indew = (special_char.index(char) - i) % 12
                decrypted_message += special_char[new_indew]
            elif char in numbers:
                new_indew = (numbers.index(char) - i) % 10
                decrypted_message += numbers[new_indew]
            else:
                decrypted_message += char
        print(decrypted_message, "    the key of encryption was: ", i)
        decrypted_message = ''

#Ask to user what he wants to do

will = input("Que veux tu faire? ")
if will == 'd':
    message = input("Quel message veux tu décrypter")
    print("######  Decoded solution  ######")
    cesar_bf(message)
    print("################################")
elif will == 'c':
    message = cesar_encrypt()
    print(" ")
    print("######  Encoded message   ######")
    print(message)
    print("################################ ")
elif will == "c et d":
    message = cesar_encrypt()
    print(" ")
    print("######  Encoded message   ######")
    print(message)
    print("################################ ")
    print(" ")
    print("######  Decoded solution  ######")
    cesar_bf(message)
    print("################################")