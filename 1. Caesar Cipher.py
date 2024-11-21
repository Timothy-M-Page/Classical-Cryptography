
A = "abcdefghijklmnopqrstuvwxyz"

def caesar(p,k):
    c = ""
    for l in p:
        if l in A:
            c = c + A[(A.index(l) + k) % 26]
        else:
            c = c + l
    return c

def caesar_decrypt(c,k):
    p = ""
    for l in c:
        if l in A:
            p = p + A[(A.index(l) - k) % 26]
        else:
            p = p + l
    return p




