from math import gcd

def egcd(a, b):
    if a == 0:
        return b, 0, 1
    g, y, x = egcd(b % a, a)
    return g, x - (b // a) * y, y

def modinv(a, m):
    g, x, _ = egcd(a, m)
    if g != 1:
        raise Exception('No modular inverse')
    return x % m

def rsa_key_reuse_attack(c1, c2, e1, e2, n):
    g, s1, s2 = egcd(e1, e2)
    if g != 1:
        raise Exception('Exponents not coprime')
    m1 = pow(c1, s1, n) if s1 >= 0 else modinv(pow(c1, -s1, n), n)
    m2 = pow(c2, s2, n) if s2 >= 0 else modinv(pow(c2, -s2, n), n)
    return (m1 * m2) % n

p, q = 61, 53
n = p * q
e1, e2 = 17, 23
m = 42
c1 = pow(m, e1, n)
c2 = pow(m, e2, n)

recovered = rsa_key_reuse_attack(c1, c2, e1, e2, n)
print("Original Message :", m)
print("Recovered Message:", recovered)
#output
Original Message : 42
Recovered Message: 42

