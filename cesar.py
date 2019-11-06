#Author: Yuxuama

#Declaration of dedicated alphabet

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_char = "!?:;.,'éèàçù-"
numbers = "0123456789"

#French data base for statistic attack

statistic_french_base = [['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'], \
                         [7.11, 1.14, 3.18, 3.67, 12.10, 1.11, 1.23, 1.11, 6.59, 0.34, 0.29, 4.96, 2.62, 6.39, 5.02, 2.49, 0.65, 6.07, \
                          6.51, 5.92, 4.49, 1.11, 0.17, 0.38, 0.46, 0.15]]


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


def cesar_uncrypt(chain, key):
    decrypted_message = ''
    for char in chain:
        if char in lowercase:
            new_indew = (lowercase.index(char) - key) % 26
            decrypted_message += lowercase[new_indew]
        elif char in uppercase:
            new_indew = (uppercase.index(char) - key) % 26
            decrypted_message += uppercase[new_indew]
        elif char in special_char:
            new_indew = (special_char.index(char) - key) % 13
            decrypted_message += special_char[new_indew]
        elif char in numbers:
            new_indew = (numbers.index(char) - key) % 10
            decrypted_message += numbers[new_indew]
        else:
            decrypted_message += char
    return decrypted_message

## Computation of all solution for a given coded chain ##

def cesar_bf(chain):
    decrypted_message = ''
    for i in range(1, 26):
        decrypted_message = cesar_uncrypt(chain, i)
        print(decrypted_message, "    the key of encryption was: ", i)


## Cryptography statistic analysis ##

def cesar_cs(chain, error):
    #Creation of work table
    work_table = [["Charactères"], \
                  ["Effectifs  "], \
                  ["Fréquence  "], \
                  ["Sugsestion "]]
    total_effectif = 0

    #Transform all char in lowercase for statistic processing
    for char in range(len(chain)):
        chain[char].lower()

    #  Statistic Analysis  #
    for char in chain:
        if work_table[0].count(char) == 0:
            if char != ' ':
                work_table[0].append(char)
                work_table[1].append(1)
        else:
            index = work_table[0].index(char)
            work_table[1][index] += 1
    #Computing frequences (via total effectif)
    for i in range(2):
        for number in work_table[1]:
            if type(number) is not str:
                if i == 0:
                    total_effectif += number
                else:
                    work_table[2].append(round((number / total_effectif) * 100, 2))

    #Compare with data base
    base = statistic_french_base
    maxi_proche = [0, 'NA']
    for index in range(1, len(work_table[0])):
        for base_i in range(len(base[0])):
            if base[1][base_i] - error < work_table[2][index] < base[1][base_i] + error:
                proche = base[1][base_i]/work_table[2][index]
                sugested_char = base[0][base_i]
                if maxi_proche[0] < proche:
                    maxi_proche[1] = sugested_char
                maxi_proche[0] = max(maxi_proche[0], proche)
        work_table[3].append(maxi_proche[1])
        maxi_proche = [0, 'NA']

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
while 1:
    will = int(input(">>> "))
    if will == 1:
        message = cesar_encrypt()
        print(" ")
        print("======  Encoded message   ", "="*45)
        print(message)
        print("="*70)
        break
    elif will == 2:
        message = input("Quel message veux tu décrypter ")
        print("======  Decoded solution  ", "="*50)
        cesar_bf(message)
        break
    elif will == 3:
        message = cesar_encrypt()
        print(" ")
        print("======  Encoded message   ", "="*45)
        print(message)
        print("="*70)
        print(" ")
        print("======  Decoded solution  ", "="*50)
        cesar_bf(message)
        break
    elif will == 4:
        message = cesar_encrypt()
        print(" ")
        print("======  Encoded message   ", "="*45)
        print(message)
        print("="*70)
        print(" ")
        print("======  Crypto Analysis   ", "="*45)
        cesar_cs(message, 0.5)
        break
    elif will == 5:
        print("See you soon")
        break
    else:
        print("Commande invalide")
