
A = "abcdefghijklmnopqrstuvwxyz"

def Atbash(p):
    c = ""
    for l in p:
        c = c + A[25 - A.index(l)]
    return(c)

