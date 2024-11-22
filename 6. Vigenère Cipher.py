A = "abcdefghijklmnopqrstuvwxyz"

def vigenere_encrypt(p,key):
    c = ""
    i = 0
    for l in p:
        if l in A:
            a = A.index(l)
            b = key[i % len(key)]
            d = A.index(b)
            c += A[(a+d) % len(A)]
            i += 1
        else:
            c += l
    return c

def vigenere_decrypt(c,key):
    p = ""
    i = 0
    for l in c:
        if l in A:
            a = A.index(l)
            b = key[i % len(key)]
            d = A.index(b)
            p += A[(a-d) % len(A)]
            i += 1
        else:
            p += l
    return p


