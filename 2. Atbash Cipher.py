
A = "abcdefghijklmnopqrstuvwxyz"

def Atbash(p):
    c = ""
    for l in p:
        if l in A:
            c = c + A[25 - A.index(l)]
        else:
            c = c + l
    return(c)

# Note that the Atbash cipher is its own inverse.
