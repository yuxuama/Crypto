"""
Cryptage avec Cesar
Fait par Alexandre 

"""

alphabetlower = "abcdefghijklmnopqrstuvwxyz"
alphabetupper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


#fonction pour crypter
def crypt():

    while True:
        motclear = input("Texte: ")
        for letters in motclear:
            if letters not in alphabetlower and letters not in alphabetupper:
                print("Veuillez mettre un texte")
                crypt()
        break
    while True:
        try:
            key = int(input("Decallage: "))
            if key < 0:
                raise ValueError
            elif key > 26:
                while key > 26:
                    key -= 26
                break
        except ValueError:
            print('Veuillez mettre un nombre supèrieur à 0')
            continue
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

#fonction pour decrypter
def uncrypt():
    print("Pas encore fait")

#fonction pour bruteforce
def bruteforce():
    print("Pas encore fait")

#affichage menu
print("="*60)
print("1 Crypt")
print("2 Uncrypt")
print("3 Bruteforce")
print("4 Quit")
print("="*60)


while True:
    
    try:
        choix = int(input(">>> "))
        
        if choix == 1:
            crypt()
            continue
        elif choix == 2:
            uncrypt()
            continue
        elif choix == 3:
            bruteforce()
            continue
        elif choix == 4:
            break
        else:
            raise ValueError
    except ValueError:
        print("Incorrect Value")
        continue