def egcd(a, b):
    if a == 0:
        return b, 0, 1
    g, y, x = egcd(b % a, a)
    return g, x - (b // a) * y, y

def modinv(e, phi):
    g, x, _ = egcd(e, phi)
    if g != 1:
        raise Exception('modular inverse does not exist')
    return x % phi

p = 61
q = 53
n = p * q
phi = (p - 1) * (q - 1)
e = 17
d = modinv(e, phi)

print("Public Key (n, e):", (n, e))
print("Private Key (n, d):", (n, d))
#output

Public Key (n, e): (3233, 17)
Private Key (n, d): (3233, 2753)
