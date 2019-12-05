##################################
####      Vigenere Attack     ####
##################################

lowercase = "abcdefghijklmnopqrstuvwxyz"
statistic_french_base_c = [7.11, 1.14, 3.18, 3.67, 12.10, 1.11, 1.23, 1.11, 6.59, 0.34, 0.29, 4.96, 2.62, 6.39, 5.02, 2.49, 0.65, 6.07,6.51, 5.92, 4.49, 1.11, 0.17, 0.38, 0.46, 0.15]
prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def vigenere_crack(chain=str):
    # Input: "chain"(string) -> It is the Vigenere coded message
    # Outputs: "decoded_chain"(string)
    #          "key"(string) -> key with which the message hes been coded

    Decoded_message = ''
    Key = ''
    
    # Sort the char of Vigenere sequences in order to save only those which belong to "lowercase"
    chain = chain.lower()
    sorted_chain = ''
    for char in chain:
        if char in lowercase:
            sorted_chain = sorted_chain + char

    # Algorythm that remark the repetition of the text and compute their distance
    repeated_chain = [[], []]  # Var which will save the repeated chains and their distances
    max_length = 6       # Set the max length of a repeated chain
    min_length = 3       # Set the min length of a repeated chain
    n_value = 3          # Set the number of value we want per length
    for length in range(min_length, max_length+1):
        count = 0
        for x in range(len(sorted_chain)):
            if count >= n_value:
                break
            if x+length < len(sorted_chain):
                tampon_chain = ''.join(sorted_chain[x+b] for b in range(length))
                if repeated_chain[0].count(tampon_chain) != 0:
                    continue
            else:
                break
            for i in range(x+length, len(sorted_chain)):
                if count >= n_value:
                    break
                if i+length < len(sorted_chain):
                    tested_chain = ''.join(sorted_chain[i+b] for b in range(length))
                    if tested_chain == tampon_chain:
                        distance = abs(i - x)
                        repeated_chain[0].append(tampon_chain)
                        repeated_chain[1].append(distance)
                        count += 1
                else:
                    break   

    ## Search for the length of the key  ##
    factor_list = []
    length_key = 0
    maximum = [0, 0, 1]
    # Computing all possible factor
    for distance in range(len(repeated_chain[1])):
        factor = decompose(repeated_chain[1][distance])
        for number in factor:
            factor_list.append(number)
    for number_index in range(len(factor_list)):
        count = factor_list.count(factor_list[number_index])
        if count <= len(repeated_chain[1]):
            maximum = [max(factor_list.count(count), length_key), number_index, 1]
        elif count % len(repeated_chain[1]) == 0:
            maximum = [max(factor_list.count(count), length_key), number_index, count/len(repeated_chain[1])]

    length_key = factor_list[maximum[1]] ** maximum[2]
    print(length_key, factor_list)




# Method that decompose an integer into prime numbers
def decompose(n=int):
    # Input: "n"(int) -> Number we want to decompose
    # Output: "decomposed_n"(list) -> Return all the prime number of the decomposition
    diviseur_index = 0
    decomposed_n = []
    while n > 2:
        number = prime_numbers[diviseur_index]
        if n % number == 0:
            decomposed_n.append(number)
            n = n/number
        if diviseur_index < len(prime_numbers) - 1:
            diviseur_index += 1
        else:
            diviseur_index = 0
    return decomposed_n


# Tests
vigenere_crack("XAUNM EESYI EDTLL FGSNB WQUFX PQTYO RUTYI INUMQ IEULS MFAFX GUTYB XXAGB HMIFI IMUMQ IDEKR IFRIR ZQUHI ENOOO IGRML YETYO VQRYS IXEOK IYPYO IGRFB WPIYR BQURJ IYEMJ IGRYK XYACP PQSPB VESIR ZQRUF REDYJ IGRYK XBLOP JARNP UGEFB WMILX MZSMZ YXPNB PUMYZ MEEFB UGENL RDEPB JXONQ EZTMB WOEFI IPAHP PQBFL GDEMF WFAHQ")