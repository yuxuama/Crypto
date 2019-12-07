####  FINAL VERSION ####

# Authors:
   # Antonin DUDRAGNE #
   # Alexandre CORNET #
   # Matthieu LECOMTE #

# Imports
from Vigenere_attack import vigenere_crack

# Declaration of dedicated alphabet
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_char = "!?:;.,'-`"
special_a = "àâ"
special_e = "éèê"
special_u = "ùû"
special_c = "ç"
numbers = "0123456789"

# French data base for statistic attack:
# For cesar
statistic_french_base_c = [7.11, 1.14, 3.18, 3.67, 12.10, 1.11, 1.23, 1.11, 6.59, 0.34, 0.29, 4.96, 2.62, 6.39, 5.02, 2.49, 0.65, 6.07,6.51, 5.92, 4.49, 1.11, 0.17, 0.38, 0.46, 0.15]
# For vigenere
statistic_french_base_v = [8.4, 1.06, 3.03, 4.18, 17.26, 1.12, 1.27, 0.92, 7.34, 0.31, 0.05, 6.01, 2.96, 7.13, 5.26, 3.01,0.99, 6.55, 8.08, 7.07, 5.74, 1.32, 0.04, 0.45, 0.3, 0.12]

####################################################
####            Interface Function              ####
####################################################
             
def user_interface():
    # Main menu
    print("======  Main menu   ", "="*34)
    print("1 Cesar methods")
    print("2 Vigenere methods")
    print("3 Beaufort methods")
    print("4 Quit")
    print("="*55)
    cmd = int(input(">>> "))
    if cmd == 1:
        cesar_interface()
    elif cmd == 2:
        vigenere_interface()
    elif cmd == 3:
        beaufort_interface()
    elif cmd == 4:
        print("See you soon")

# Interface for cesar encryption
def cesar_interface():
    #Display the menu
    print("=" * 55)
    print("1 Crypt", "              Crypt a message ")
    print("2 Uncrypt", "            Uncrypt a message")
    print("3 Bruteforce", "         Attack with brute force")
    print("4 Crypto Analysis", "    Attack with statistic method")
    print("5 Return to main menu")
    print("6 Quit")
    print("=" * 55)
    while 1:
        cmd = int(input(">>> "))
        if cmd == 1:
            infos = ask("cesar")
            print("Crypted message: ", cesar_encrypt(infos[0], infos[1]))
        elif cmd == 2:
            infos = ask("cesar")
            print("Decrypted message: ", cesar_decrypt(infos[0], infos[1]))
        elif cmd == 3:
            infos = input("Crypted message: ")
            cesar_bf(infos)
        elif cmd == 4:
            infos = input("Crypted message: ")
            crypto_analyse_stats(infos, 2, "c")
        elif cmd == 5:
            user_interface()
            break
        elif cmd == 6:
            print("See you soon")
            break
        else:
            print("Invalid command")
            continue
 
# Interface for vigenere encryption
def vigenere_interface():  
    # Display the menu on console
    print("="*55)
    print("1 Crypt")
    print("2 Uncrypt")
    print("3 Crack Vigenere (beta test)")
    print("4 Crypto Analysis")
    print("5 Return to main menu")
    print("6 Quit")
    print("="*55)
    while 1:
        cmd = int(input(">>> "))
        if cmd == 1:
            infos = ask("v")
            print("Crypted message: ", vigenere_encrypt(infos[0], infos[1]))
        elif cmd == 2:
            infos = ask("v")
            print("Decrypted message: ", vigenere_decrypt(infos[0], infos[1]))
        elif cmd == 3:
            info = input("Crypted message: ")
            key = vigenere_crack(info)
            print("The key was: ", key)
            print("Decrypted message: ", vigenere_decrypt(info, key))
        elif cmd == 4:
            info = input("Crypted message: ")
            crypto_analyse_stats(info, 2, "v")
        elif cmd == 5:
            user_interface()
            break
        elif cmd == 6:
            print("See you soon")
            break
        else:
            print("Invalid command")
            continue

# Interface for Beaufort encryption
def beaufort_interface():
    print("=" * 55)
    print("1 Crypt")
    print("2 Uncrypt")
    print("3 Return to main menu")
    print("4 Quit")
    print("=" * 55)
    while 1:
        cmd = int(input(">>> "))
        if cmd == 1:
            infos = ask("v")
            print("Crypted message: ", vigenere_decrypt(infos[0], infos[1]))  # We've just inverted the two method of vigenere in order to compute Beaufort's ones
        elif cmd == 2:
            infos = ask("v")
            print("Decrypted message: ", vigenere_encrypt(infos[0], infos[1]))
        elif cmd == 3:
            user_interface()
            break
        elif cmd == 4:
            print("See you soon :)")
            break
        else:
            print("Invalid command")

# Input method  
def ask(method):
    # Receive chain (method) -> it identifies rather cesar method or an other
    while 1:
        message = input("Text: ")
        key = input("Key: ")
        if method == "cesar":
            try:
                key = int(key)
                if not 0 < key < 26:
                    print("La clé doit être comprise entre 0 et 25")
                    continue
                return message, key
            except ValueError:
                print("La clé doit être comprise entre 0 et 25")
                continue
        else:
            cmpt = 0
            for letter in key:
                if letter in lowercase:
                    cmpt += 1
                elif letter in uppercase:
                    cmpt += 1
            if cmpt == len(key):
                return message, key
            else:
                print("La clé doit être composée de lettres de l'alphabet")
                continue

###############################################
####        Cesar encryption methods       ####
###############################################

def cesar_encrypt(chain, key):
    # Receive chain(string) = string to encrypt
    # Receive key(int) = key with which "chain" will be encrypt
    # Output = "crypted_message"(string)
    crypted_message = ''

    for char in chain:
        if char in lowercase:
            new_index = (lowercase.index(char) + key) % 26
            crypted_message += lowercase[new_index]
        elif char in uppercase:
            new_index = (uppercase.index(char) + key) % 26
            crypted_message += uppercase[new_index]
        elif char in numbers:
            new_index = (numbers.index(char) + key) % 10
            crypted_message += numbers[new_index]
        elif char in special_e:
            new_index = (lowercase.index("e") + key) % 26
            crypted_message += lowercase[new_index]
        elif char in special_a:
            new_index = (lowercase.index("a") + key) % 26
            crypted_message += lowercase[new_index]
        elif char in special_c:
            new_index = (lowercase.index("c") + key) % 26
            crypted_message += lowercase[new_index]
        elif char in special_u:
            new_index = (lowercase.index("u") + key) % 26
            crypted_message += lowercase[new_index]
        else:
            crypted_message += char
    return crypted_message


def cesar_decrypt(chain, key):
    # Receive chain(string) = string to decrypt
    # Receive key(int) = key with which "chain" will be decrypt
    # Output = "decrypted_message"(string)
    decrypted_message = ''

    for char in chain:
        if char in lowercase:
            new_indew = (lowercase.index(char) - key) % 26
            decrypted_message += lowercase[new_indew]
        elif char in uppercase:
            new_indew = (uppercase.index(char) - key) % 26
            decrypted_message += uppercase[new_indew]
        elif char in numbers:
            new_indew = (numbers.index(char) - key) % 10
            decrypted_message += numbers[new_indew]
        else:
            decrypted_message += char
    return decrypted_message

def cesar_bf(chain):
    # Receive chain(string) = string to attack
    for i in range(1, 26):
        decrypted_message = cesar_decrypt(chain, i)
        print(decrypted_message, "    the key of encryption was: {0}".format(i))
        


###################################################
####        Vigenere encryption methods        ####
###################################################

def vigenere_encrypt(chain, key):
    # Receive chain(string) = string to encrypt
    # Receive key(string) = key with which "chain" will be encrypt
    # Output = "crypted_message"(string)
    cmpt = 0
    motcrypt = ''
    key = key.lower()

    for letters in chain:
        if letters in lowercase:
            number = (lowercase.index(letters) + lowercase.index(key[cmpt])) % 26
            motcrypt += lowercase[number]
            cmpt = (cmpt + 1) % len(key)
        elif letters in uppercase:
            number = (uppercase.index(letters) + lowercase.index(key[cmpt])) % 26
            motcrypt += uppercase[number]
            cmpt = (cmpt + 1) % len(key)
        elif letters in special_e:
            number = (lowercase.index("e") + lowercase.index(key[cmpt])) % 26
            motcrypt += lowercase[number]
            cmpt = (cmpt + 1) % len(key)
        elif letters in special_a:
            number = (lowercase.index("a") + lowercase.index(key[cmpt])) % 26
            motcrypt += lowercase[number]
            cmpt = (cmpt + 1) % len(key)
        elif letters in special_c:
            number = (lowercase.index("c") + lowercase.index(key[cmpt])) % 26
            motcrypt += lowercase[number]
            cmpt = (cmpt + 1) % len(key)
        elif letters in special_u:
            number = (lowercase.index("u") + lowercase.index(key[cmpt])) % 26
            motcrypt += lowercase[number]
            cmpt = (cmpt + 1) % len(key)
        else:
            motcrypt += letters



    return motcrypt

def vigenere_decrypt(chain, key):
    # Receive chain(string) = string to decrypt
    # Receive key(string) = key with which "chain" will be decrypt
    # Output = "decrypted_message"(string)
    cmpt = 0
    motcrypt = ''
    key = key.lower()

    for letters in chain:
        if letters in lowercase:
            number = (lowercase.index(letters) - lowercase.index(key[cmpt])) % 26
            motcrypt += lowercase[number]
            cmpt = (cmpt + 1) % len(key)
        elif letters in uppercase:
            number = (uppercase.index(letters) - lowercase.index(key[cmpt])) % 26
            motcrypt += uppercase[number]
            cmpt = (cmpt + 1) % len(key)
        else:
            motcrypt += letters


    return motcrypt

###################################################
####         Cryptanalyse statistique           ###
###################################################

def crypto_analyse_stats(chain, error, method):
    # Input: chain(string) -> message we have to analyse
    #        error(int) -> give the precision of the suggestion algorithm
    #        method(string) -> is used to choose the correct database
    # Output: built table in console with 4 rows (Charactère, Effectif, Fréquence et Suggestion)

    #Choose the database in function of the method used
    if method == "c":
        base = statistic_french_base_c
    else:
        base = statistic_french_base_v

    #Transform character into lowercase
    chain = chain.lower()

    #Creation of work table (statistic table)
    work_table = [["Charactères"], \
                  ["Effectifs  "], \
                  ["Fréquence  "], \
                  ["Suggestion "]]
    total_effectif = 0

    #  Statistic Analysis  #
    for char in chain:
        if work_table[0].count(char) == 0:
            if char != ' ' and not char in special_char:
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

    # Sort of the "worktable"  characteres in order to save only those which are in "lowercase"

    for char in work_table[0]:
        if not char == "Charactères" and not char in lowercase:
            work_table[0].remove(char)

    #Compare with data base # return the value of database that fit the best to computing frequences, if there is not: return 'NA'
    maxi_proche = [0, 'NA']   #Save var to choose the best char (see below)
    for index in range(1, len(work_table[0])):
        for base_i in range(len(base)):
            if base[base_i] - error < work_table[2][index] < base[base_i] + error:    #testing if frequence value is in range
                rapport = work_table[2][index]/base[base_i]    #Compute how close the two values are
                sugested_char = lowercase[base_i]
                if maxi_proche[0] < rapport:  # If precedent save quotient is smaller, redefine the suggested char value
                    maxi_proche[1] = sugested_char
                maxi_proche[0] = max(maxi_proche[0], rapport)
        work_table[3].append(maxi_proche[1])
        maxi_proche = [0, 'NA']

    # Display work_table with a clean print table
    for i in range(4):
        for j in range(len(work_table[0])):
            char = work_table[i][j]
            if type(char) is str:
                lenght = len(char)
                if lenght < 5:
                    char += ' ' * (5 - lenght)
            elif type(char) is int or type(char) is float:
                char = str(char)
                lenght = len(char)
                if lenght < 5:
                    char += ' ' * (5 - lenght)
            print("|", char, end='')
        print('||')

# Run
user_interface()