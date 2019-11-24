"""
Chiffre de Vigneère
Made by Alexandre

"""

alphabetlower = "abcdefghijklmnopqrstuvwxyz"
alphabetupper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
dico = ["test", "lol", "prof"]

#fonction pour demander la key et le message
def texte():
    mot = input("Texte: ")
    while True:
        try:
            key = input("Key: ")
            for elements in key :
                if elements not in alphabetlower and elements not in alphabetupper:
                    raise ValueError
                elif elements == " ":
                    raise ValueError
            key = key.lower()
            return mot, key
        except ValueError:
            print('Veuillez mettre que des lettres.')
            continue 

#fonction pour crypter
def crypt(mot, key):
    cmpt = 0
    motcrypt = ''

    for letters in mot:
        if letters not in alphabetlower and letters not in alphabetupper:
            motcrypt += letters
        else:
            if letters in alphabetlower:
                chiffre = alphabetlower.index(letters) + alphabetlower.index(key[cmpt])
                while chiffre >= 26:
                    chiffre -= 26
                motcrypt += alphabetlower[chiffre]
            else:
                chiffre = alphabetupper.index(letters) + alphabetlower.index(key[cmpt])
                while chiffre >= 26:
                    chiffre -= 26
                motcrypt += alphabetupper[chiffre]

            cmpt += 1

            if cmpt == len(key):
                cmpt = 0

    print('Mot crypté:',motcrypt)
  
#fonction pour decrypter
def uncrypt(mot, key):
    cmpt = 0
    motcrypt = ''

    for letters in mot:
        if letters not in alphabetlower and letters not in alphabetupper:
            motcrypt += letters
        else:
            if letters in alphabetlower:
                chiffre = alphabetlower.index(letters) - alphabetlower.index(key[cmpt])
                while chiffre <= -1:
                    chiffre += 26
                motcrypt += alphabetlower[chiffre]
            else:
                chiffre = alphabetupper.index(letters) - alphabetlower.index(key[cmpt])
                while chiffre <= -1:
                    chiffre += 26
                motcrypt += alphabetupper[chiffre]

            cmpt += 1

            if cmpt == len(key):
                cmpt = 0

    print('Mot decrypté:',motcrypt)

#fonction pour faire une attaque par dictionnaire
def attackdico():
    mot = input("Texte: ")
    for elements in dico:
        print("")
        uncrypt(mot, elements)
        print("Key :",elements)

#affichage menu
print("="*60)
print("1 Crypt")
print("2 Uncrypt")
print("3 Attaque Dictionnaire")
print("4 Quit")
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
            attackdico()
            continue
        elif choix == 4:
            break
        else:
            raise ValueError
    except ValueError:
        print("Incorrect Value")
        continue
