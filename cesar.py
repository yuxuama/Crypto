"""
Cryptage avec Cesar
Fait par Alexandre 

"""

alphabetlower = "abcdefghijklmnopqrstuvwxyz"
alphabetupper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


#fonction pour crypter
def crypt():

    motclear = input("Texte: ")
    motcrypt = ''

    while True:
        try:
            key = int(input("Key: "))
            if key < 0:
                raise ValueError
            elif key > 26:
                while key > 26:
                    key -= 26
                break
            else:
                break
        except ValueError:
            print('Veuillez mettre un nombre supèrieur à 0')
            continue

    for letters in motclear :
        if letters not in alphabetlower and letters not in  alphabetupper:
            motcrypt += letters
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
    print("Message Crypt: ",motcrypt)

#fonction pour decrypter
def uncrypt():
   
    motclear = input("Texte: ")
    motuncrypt = ''

    while True:
        try:
            key = int(input("Key: "))
            if key < 0:
                raise ValueError
            elif key > 26:
                while key > 26:
                    key -= 26
                break
            else:
                break
        except ValueError:
            print('Veuillez mettre un nombre supèrieur à 0')
            continue
    
    for letters in motclear :
        if letters not in alphabetlower and letters not in alphabetupper:
            motuncrypt += letters
            continue
        if letters in alphabetlower:
            chiffre = alphabetlower.index(letters) - key
            if chiffre <= -1 :
                chiffre += 26
            motuncrypt += alphabetlower[chiffre]
        else:
            chiffre = alphabetupper.index(letters) - key
            if chiffre <= -1 :
                chiffre += 26
            motuncrypt += alphabetupper[chiffre]
    print("Message Uncrypt: ",motuncrypt)

#fonction pour bruteforce
def bruteforce():
    print("Pas encore fait")

#fonction pour analyse statistic
def statistic():
    print("Pas encore fait")

#affichage menu
print("="*60)
print("1 Crypt")
print("2 Uncrypt")
print("3 Bruteforce")
print("4 Statistic")
print("5 Quit")
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
            statistic()
            continue
        elif choix == 5:
            break
        else:
            raise ValueError
    except ValueError:
        print("Incorrect Value")
        continue