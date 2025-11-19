import numpy as np
from sympy import Matrix

def text_to_matrix(text, n):
    return [ord(c) - ord('A') for c in text.upper() if c.isalpha()][:n*n]

def matrix_to_text(matrix):
    return ''.join(chr(int(val) % 26 + ord('A')) for val in matrix)

def mod_inverse_matrix(matrix, modulus):
    return Matrix(matrix).inv_mod(modulus)

def hill_attack(plaintext, ciphertext, n=2):
    pt_matrix = np.array(text_to_matrix(plaintext, n)).reshape(n, n)
    ct_matrix = np.array(text_to_matrix(ciphertext, n)).reshape(n, n)

    pt_inv = mod_inverse_matrix(pt_matrix, 26)
    key_matrix = (pt_inv * Matrix(ct_matrix)) % 26

    return key_matrix

def demo():
    plaintext = "HELP"
    ciphertext = "ZEBB"

    print("📨 Known Plaintext :", plaintext)
    print("🔒 Ciphertext      :", ciphertext)

    key = hill_attack(plaintext, ciphertext)
    print("🧮 Recovered Key Matrix:")
    print(np.array(key).astype(int))

if __name__ == "__main__":
    demo()
#output
📨 Known Plaintext : HELP
🔒 Ciphertext      : ZEBB
🧮 Recovered Key Matrix:
[[3 10]
 [20 9]]

