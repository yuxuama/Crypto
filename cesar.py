
"""Encoding a message with Cesar process"""

def encrypt():
    key = int(input("Donne une clé de codage: "))
    if not 0 < key < 26:
        raise ValueError("La clé de codage doit être comprise entre 0 et 26")
    message = input("Donne le message que tu veux crypter: ")
    crypted_message = ''
    for char in message:
        if char != ' ' or char != ',':
            crypted_message = crypted_message + chr(ord(char) + key)
        else:
            crypted_message = crypted_message + char
    return crypted_message

print(encrypt())