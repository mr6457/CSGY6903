# c = (ax + b) mod 26
# https://en.wikipedia.org/wiki/Affine_cipher
# https://crypto.stackexchange.com/questions/25568/affine-cipher-calculate-the-key-from-a-known-plaintext-ciphertext-pair
# https://math.stackexchange.com/questions/2118060/affine-cipher-finding-the-decryption-map
#Eve has the ciphertext “QJKESREOGHGXXREOXEO”. She magically knows the cipher is an
#affine cipher and the letter T is encrypted to H and O to E. Recover the decryption function and decipher
#the message. Students can solve it manually. They can also solve it by a computer program. They both
#shall give the same results. Remember, the code shall be more general, not just in this case. Submit both
#results.

ls = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#Ciphertext = QJKESREOGHGXXREOXEO
#Known encrypted pairs
#  T -> H ; O -> E

ciphertext = "QJKESREOGHGXXREOXEO"
knownpair1 = ['T','H']
knownpair2 = ['O','E']

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
    if ( ( (ls.index(knownpair1[0]) - ls.index(knownpair2[0])) * a) % 26 == ls.index(knownpair1[1]) - ls.index(knownpair2[1])  ):
        print(f"a = {a}")
        for b in range(26):
            if ( ls.index(knownpair1[1]) == ( a * ls.index(knownpair1[0]) + b ) % 26 ): 
                print(f"b = {b}")
                print(affine_dec(a,b,ciphertext)) 


