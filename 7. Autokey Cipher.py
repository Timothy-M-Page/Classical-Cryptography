A = "abcdefghijklmnopqrstuvwxyz"

def autokey_encrypt(p, key):
    key2 = key + p
    c = ""
    i = 0
    for l in p:
        if l in A:
            a = A.index(l)
            b = key2[i]
            d = A.index(b)
            c += A[(a+d) % len(A)]
            i += 1
        else:
            c += l
    return c

def autokey_decrypt(c, key):
    key2 = key
    p = ""
    i = 0
    for l in c:
        if l in A:
            a = A.index(l)
            b = key2[i]
            d = A.index(b)
            p += A[(a-d)%len(A)]
            key2 += p[i]
            i += 1
        else:
            p += l
    return p


