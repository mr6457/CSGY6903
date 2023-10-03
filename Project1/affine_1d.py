# c = (ax + b) mod 26
# T -> H ; O -> E
# https://en.wikipedia.org/wiki/Affine_cipher
# https://crypto.stackexchange.com/questions/25568/affine-cipher-calculate-the-key-from-a-known-plaintext-ciphertext-pair
# https://math.stackexchange.com/questions/2118060/affine-cipher-finding-the-decryption-map
# solve a

ciphertext = "QJKESREOGHGXXREOXEO"
ls = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def affine(a,b,plaintext):
    plaintext = plaintext.upper()
    ciphertext = ""
    for letter in plaintext:
        c = (a * ls.index(letter) + b ) % 26
        ciphertext+=ls[c]
    return(ciphertext)

def affine_dec(a,b,ciphertext):
    ciphertext = ciphertext.upper()
    # find modular multiplicative inverse of a
    for i in range(26):
        if a*i%26 == 1:
            a = i
    plaintext = ""
    for letter in ciphertext:
        p = ( a * ( ls.index(letter) - b ) ) % 26
        plaintext += ls[int(p)]
    return(plaintext)




for a in range(26):
    if ( ( (ls.index("T") - ls.index("O")) * a) % 26 == ls.index("H") - ls.index("E")  ):
        print(f"a = {a}")
        for b in range(26):
            if ( ls.index("H") == ( a * ls.index("T") + b ) % 26 ): 
                print(f"b = {b}")
                print(affine_dec(a,b,ciphertext)) 


