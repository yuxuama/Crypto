"""

Cryptage avec Cesar

"""



alphabet = "abcdefghijklmnopqrstuvwxyz"
motclear = input("Texte: ").lower()
key = int(input("Decallage: "))
motcrypt = ''


for letters in motclear :
    chiffre = alphabet.index(letters) + key
    if chiffre > 26 :
        chiffre -=26
    motcrypt += alphabet[chiffre]
print("Mot Crypt: ",motcrypt)
