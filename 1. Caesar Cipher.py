
A = "abcdefghijklmnopqrstuvwxyz"

def caesar_encrypt(p,k):
    c = ""
    p = p.lower()
    for l in p:
        if l in A:                            # For each alphabetic character in the plaintext
            c += A[(A.index(l) + k) % 26]     # shift the character k places in the alphabet.
        else:
            c += l
    return c

def caesar_decrypt(c,k):
    p = ""
    for l in c:
        if l in A:
            p += A[(A.index(l) - k) % 26]    # Shift the alphabetic characters back by k places. 
        else:
            p += l
    return p




