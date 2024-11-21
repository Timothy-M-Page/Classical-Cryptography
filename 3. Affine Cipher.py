

A = "abcdefghijklmnopqrstuvwxyz"

def inv(a):                             # Inverse element in the group Z/26Z
    for x in range(1,26):
        if a*x % 26 == 1:
            return x
    print(f"{a} has no inverse mod 26")  # Error message if gcd(a,26) > 1.
    return None

def affine_encrypt(a,b,p):
    c = ""
    for i in p:
        if i in A:
            c += A[(b + (a*A.index(i))) % 26]
        else:
            c += i
    return c

def affine_decrypt(a,b,c):
    p = ""
    x = inv(a)
    if x is None:
        return "Decryption failed due to no inverse"
    for i in c:
        if i in A:
            p += A[((A.index(i) - b) * x) % 26]
        else:
            p += i
    return p


