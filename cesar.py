"""
Cryptage avec Cesar
Fait par Alexandre (cette version)

"""

alphabetlower = "abcdefghijklmnopqrstuvwxyz"
alphabetupper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#fonction pour crypter
def crypt():

    motclear = input("Texte: ")
    key = int(input("Decallage: "))
    motcrypt = ''

    for letters in motclear :
        if letters == " ":
            motcrypt += ' '
            continue
        if letters in alphabetlower:
            chiffre = alphabetlower.index(letters) + key
            if chiffre >= 26 :
                chiffre -=26
            motcrypt += alphabetlower[chiffre]
        else:
            chiffre = alphabetupper.index(letters) + key
            if chiffre >= 26 :
                chiffre -=26
            motcrypt += alphabetupper[chiffre]
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
