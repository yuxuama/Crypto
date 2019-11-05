#Author: Yuxuama

#declaration of dedicated alphabet

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_char = "!?:;.,'éèàçù-"
numbers = "0123456789"


##  Encoding a message with Cesar process  ##

def cesar_encrypt():

    # Asking for key
    try:
        key = int(input("Donne une clé de codage: "))
        if not 0 < key < 26:      #Check if the key is in the range for a Cesar encode
            raise ValueError("La clé de codage doit être comprise entre 0 et 26")
    except ValueError:
        raise ValueError("Tu dois entrer un chiffre")

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
            new_index = (special_char.index(char) + key) % 13
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
                new_indew = (special_char.index(char) - i) % 13
                decrypted_message += special_char[new_indew]
            elif char in numbers:
                new_indew = (numbers.index(char) - i) % 10
                decrypted_message += numbers[new_indew]
            else:
                decrypted_message += char
        print(decrypted_message, "    the key of encryption was: ", i)
        decrypted_message = ''


## Cryptography statistic analysis ##

def cesar_cs(chain):
    #Creation of work table
    work_table = [["Charactères"], \
                  ["Effectifs  "], \
                  ["Fréquence  "], \
                  ["Sugsestion "]]
    total_effectif = 0

    #Transform all char in lowercase for statistic processing
    for char in range(len(chain)):
        if chain[char] in uppercase:
            chain[char] = lowercase[uppercase.index(chain[char])]

    #  Statistic Analysis  #
    for char in chain:
        if work_table[0].count(char) == 0:
            if char != ' ':
                work_table[0].append(char)
                work_table[1].append(int(1))
        else:
            index = work_table[0].index(char)
            work_table[1][index] += 1
    #Computing of total effectif in view to compute frequences
    for number in work_table[1]:
        if type(number) is not str:
            total_effectif += number
    #Compputing frequences
    for number in work_table[1]:
        if type(number) is not str:
            num = round((number/total_effectif)*100, 2)
            work_table[2].append(num)

    #Display work_table
    for x in range(4):
        print(work_table[x])

#Display of the menu
print("=" * 60)
print("1 Crypt")
print("2 Uncrypt")
print("3 Bruteforce")
print("4 Crypto Analysis")
print("5 Quit")
print("=" * 60)

#Ask to user what he wants to do

will = int(input(">>> "))
if will == 1:
    message = input("Quel message veux tu décrypter ")
    print("======  Decoded solution  ======")
    cesar_bf(message)
elif will == 2:
    message = cesar_encrypt()
    print(" ")
    print("======  Encoded message   ======")
    print(message)
    print("="*32)
elif will == 3:
    message = cesar_encrypt()
    print(" ")
    print("======  Encoded message   ======")
    print(message)
    print("="*32)
    print(" ")
    print("======  Decoded solution  ======")
    cesar_bf(message)
elif will == 4:
    message = cesar_encrypt()
    print(" ")
    print("======  Encoded message   ======")
    print(message)
    print("="*32)
    print(" ")
    print("======  Crypto Analysis   ======")
    cesar_cs(message)
    print("Commande invalide")
elif will == 5:
    print("See you soon")
else:
    print("Commande invalide")
