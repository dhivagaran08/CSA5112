def power_mod(base, exponent, modulus):
    return pow(base, exponent, modulus)

p = 23
g = 5
a = 6
b = 15

A = power_mod(g, a, p)
B = power_mod(g, b, p)

shared_key_a = power_mod(B, a, p)
shared_key_b = power_mod(A, b, p)

print("A:", A)
print("B:", B)
print("Shared A:", shared_key_a)
print("Shared B:", shared_key_b)
#output
A: 8
B: 2
Shared A: 13
Shared B: 13

