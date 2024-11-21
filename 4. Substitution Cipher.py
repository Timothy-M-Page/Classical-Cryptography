

A = "abcdefghijklmnopqrstuvwxyz"
B = "poiuytrewqasdfghjklmnbvcxz"    # The substitution alphabet

def sub(p, b):
    c = ""
    for l in p:
        if l in A:
            c += b[(A.index(l))]
        else:
            c += l
    return c

def sub_decrypt(c, b):
    p = ""
    for l in c:
        if l in A:
            p += A[(b.index(l))]
        else:
            p += l
    return p
