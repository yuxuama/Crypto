"""
Cryptage avec Cesar
"""

alphabet = "abcdefghijklmnopqrstuvwxyz"

#fonction pour crypter
def crypt():

    motclear = input("Texte: ").lower()
    key = int(input("Decallage: "))
    motcrypt = ''

    for letters in motclear :
        if letters == " ":
            motcrypt += ' '
            continue
        chiffre = alphabet.index(letters) + key
        if chiffre > 26 :
            chiffre -=26
        motcrypt += alphabet[chiffre]
    print("Mot Crypt: ",motcrypt)


#terminal pour les commandes
while True:
    cmd = input(">>> ")
    if cmd == 'crypt':
        crypt()
    elif cmd == 'stop':
        break
    else:
        print("Command Invalide")
