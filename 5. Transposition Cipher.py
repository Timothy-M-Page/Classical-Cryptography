
message = "Hello world!"
permutation = [8,5,7,6,4,2,3,10,9,1,0,11]

# For a given message the transposition cipher permutes the characters
# according to the given permutation.

def transposition_encrypt(p, perm):
    c = [""] * len(p)
    if len(perm) != len(p):
        return "Length of permutation list length must match the length of the plaintext"
    for i in range(len(p)):
        c[perm[i]] = p[i]
    return "".join(c)

def transposition_decrypt(c,perm):
    p = [""] * len(c)
    if len(perm) != len(c):
        return "Length of permutation list length must match the length of the ciphertext"
    for i in range(len(c)):
        p[perm.index(i)] = c[i]
    return "".join(p)














