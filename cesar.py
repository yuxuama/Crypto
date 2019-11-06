"""
Cryptage avec Cesar

"""

alphabetlower = "abcdefghijklmnopqrstuvwxyz"
alphabetupper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#fonction pour demander la key et le message
def texte():
    mot = input("Texte: ")
    while True:
        try:
            key = int(input("Key: "))
            if key < 0:
                raise ValueError
            elif key > 26:
                while key > 26:
                    key -= 26
                return mot, key
            else:
                return mot, key
        except ValueError:
            print('Veuillez mettre un nombre supèrieur à 0')
            continue

#fonction pour crypter
def crypt(mot, key):  
 
    motcrypt = ''

    for letters in mot :
        if letters not in alphabetlower and letters not in  alphabetupper:
            motcrypt += letters
        elif letters in alphabetlower:
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
def uncrypt(mot, key):

    motuncrypt = ''

    for letters in mot :
        if letters not in alphabetlower and letters not in alphabetupper:
            motuncrypt += letters
        elif letters in alphabetlower:
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
    mot = input("Texte: ")

    for i in range(1,26):
        print("Key: ",i)
        uncrypt(mot, i)

#fonction pour analyse statistic
def statistic():

    mot = input("Texte: ").lower()
    liste = []

    for letters in mot:
        if letters not in alphabetlower:
            continue
        else:
            liste.append(letters)
    
    for elements in alphabetlower:
        pourcent = (liste.count(elements)/len(liste))*100
        if pourcent > 0:
            print(elements,"=",pourcent,"%")

            

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