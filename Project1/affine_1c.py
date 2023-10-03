# c = (ax + b) mod 26
# https://en.wikipedia.org/wiki/Affine_cipher
# https://crypto.stackexchange.com/questions/25568/affine-cipher-calculate-the-key-from-a-known-plaintext-ciphertext-pair
# https://math.stackexchange.com/questions/2118060/affine-cipher-finding-the-decryption-map
# Let us assume the plaintext is made of 26 capital letters only. So, the n=26.
#Given the affine cipher c = 5p + 9 mod 26, what is the ciphertext for the plaintext “CRYPTOISFUN”.

def affine(a,b,plaintext):
    plaintext = plaintext.upper()
    letterSet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    ciphertext = ""
    for letter in plaintext:
        # c = (5p + 9) mod 26
        c = (a * letterSet.index(letter) + b ) % 26
        ciphertext+=letterSet[c]

    print(ciphertext)

if __name__ == "__main__":
    print("[+] Ciphertext for 'CRYPTOISFUN'")
    affine(5,9,"cryptoisfun")

