
A = "abcdefghijklmnopqrstuvwxyz"

def caesar(p,k):
    c = ""
    for l in p:
        c = c + A[(A.index(l) + k) % 26]
    return c

def caesar_decrypt(c,k):
    p = ""
    for l in c:
        p = p + A[(A.index(l) - k) % 26]
    return p




