from math import gcd

def modinv(a, m):
    def egcd(a, b):
        if a == 0:
            return b, 0, 1
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y
    g, x, _ = egcd(a, m)
    if g != 1:
        raise Exception('No modular inverse')
    return x % m

def rsa_common_factor_attack(n1, n2, e1, e2, c1, c2):
    p = gcd(n1, n2)
    if p == 1:
        return None
    q1 = n1 // p
    q2 = n2 // p
    phi1 = (p - 1) * (q1 - 1)
    phi2 = (p - 1) * (q2 - 1)
    d1 = modinv(e1, phi1)
    d2 = modinv(e2, phi2)
    m1 = pow(c1, d1, n1)
    m2 = pow(c2, d2, n2)
    return m1, m2

n1 = 3233      # 61 * 53
n2 = 3127      # 61 * 51
e1 = 17
e2 = 17
c1 = pow(42, e1, n1)
c2 = pow(42, e2, n2)

m1, m2 = rsa_common_factor_attack(n1, n2, e1, e2, c1, c2)
print("Recovered Message from n1:", m1)
print("Recovered Message from n2:", m2)
#output
Recovered Message from n1: 42
Recovered Message from n2: 42
