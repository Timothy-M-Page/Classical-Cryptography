
A = "abcdefghijklmnopqrstuvwxyz"

def Atbash(p):
    c = ""
    for l in p:
        if l in A:
            c += A[25 - A.index(l)]
        else:
            c += l
    return c

# Note that the Atbash cipher is its own inverse.
# Hence there is no need for a seperate encryption and decryption function. 
