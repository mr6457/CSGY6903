# 
letterSet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def affine(a,b,plaintext):
    plaintext = plaintext.upper()
    ciphertext = ""
    for letter in plaintext:
        c = (a * letterSet.index(letter) + b ) % 26
        ciphertext+=letterSet[c]
    return(ciphertext)

def affine_dec(a,b,ciphertext):
    ciphertext = ciphertext.upper()
    # find modular multiplicative inverse of a
    for i in range(26):
        if a*i%26 == 1:
            a = i
    plaintext = ""
    for letter in ciphertext:
        p = ( a * ( letterSet.index(letter) - b ) ) % 26
        plaintext += letterSet[int(p)]
    return(plaintext)
