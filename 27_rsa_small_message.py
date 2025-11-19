def integer_root(n, e):
    return int(n ** (1 / e))

def rsa_small_message_attack(c, e):
    return integer_root(c, e)

e = 3
p = 61
q = 53
n = p * q
m = 5
c = pow(m, e, n)

recovered = rsa_small_message_attack(c, e)

print("Original Message :", m)
print("Ciphertext       :", c)
print("Recovered Message:", recovered)
#output
Original Message : 5
Ciphertext       : 125
Recovered Message: 5

