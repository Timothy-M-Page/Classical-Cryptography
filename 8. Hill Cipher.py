import numpy as np
import random

A = "abcdefghijklmnopqrstuvwxyz "

def hill_encrypt(p,M):
    D = len(M)
    for i in range(D - (len(p) % D)):
        p += A[random.randint(0, 26)]      # Add random padding to ensure the plaintext is a multiple of the dimension of the matrix
    L = len(p)
    c = ""
    for i in range(L // D):                      # i ranges over blocks of the plaintext of length D
        C = []
        for j in range(D):
            C.append(A.index(p[(i * D) + j]))    # C is the i-th block of plaintext
        E = np.dot(M,C)                          # E is those elements in C transformed by the matrix A
        for x in E:
            c += A[x % len(A)]
    return c

def matrix_inverse(M):
    d = int(round(np.linalg.det(M)))
    d_mod = d % 27
    try:
        d_inv = pow(d_mod, -1, 27)
    except ValueError:
        raise ValueError(f"Matrix is not invertible due to gcd(determinant, 27) > 1.")
    adj = np.round(d * np.linalg.inv(M)).astype(int) % 27
    inv = (d_inv * adj) % 27
    return inv


def hill_decrypt(c,M):
    D = len(M)
    L = len(c)
    I = matrix_inverse(M)
    p = ""
    for i in range(L // D):
        C = []
        for j in range(D):
            C.append(A.index(c[(i * D) + j]))
        E = np.dot(I,C)
        for x in E:
            p += A[x % len(A)]
    return p




