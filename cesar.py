"""
Cryptage avec Cesar

"""

alphabetlower = "abcdefghijklmnopqrstuvwxyz"
alphabetupper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#fonction pour demander la key et le message
def texte():
    motclear = input("Texte: ")
    while True:
        try:
            key = int(input("Key: "))
            if key < 0:
                raise ValueError
            elif key > 26:
                while key > 26:
                    key -= 26
                return motclear, key
            else:
                return motclear, key
        except ValueError:
            print('Veuillez mettre un nombre supèrieur à 0')
            continue

#fonction pour crypter
def crypt(motclear, key):  
 
    motcrypt = ''

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
def uncrypt(motclear, key):

    motuncrypt = ''

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
            mot, key = texte()
            crypt(mot, key)
            continue
        elif choix == 2:
            mot, key = texte()
            uncrypt(mot, key)
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