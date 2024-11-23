
A = "abcdefghijklmnopqrstuvwxyz"
B = "poiuytrewqasdfghjklmnbvcxz"    # The substitution alphabet

def sub_encrypt(p, b):
    c = ""
    p = p.lower()
    for l in p:
        if l in A:                  # For each alphabetic character l in the plaintext, replace
            c += b[(A.index(l))]    # the letter by the corresponding letter in the substitution alphabet.
        else:
            c += l
    return c

def sub_decrypt(c, b):
    p = ""
    for l in c:
        if l in A:                  # For each alphabetic character l in the ciphertext, replace
            p += A[(b.index(l))]    # the letter by the corresponding letter in the alphabet.
        else:
            p += l
    return p


