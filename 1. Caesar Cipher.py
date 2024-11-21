
A = "abcdefghijklmnopqrstuvwxyz"

def caesar(p,k):
    c = ""
    for l in p:
        if l in A:
            c += A[(A.index(l) + k) % 26]
        else:
            c += l
    return c

def caesar_decrypt(c,k):
    p = ""
    for l in c:
        if l in A:
            p += A[(A.index(l) - k) % 26]
        else:
            p += l
    return p




