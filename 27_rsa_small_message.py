import string

A = string.ascii_uppercase
def L2I(c): return A.index(c)
def I2L(i): return A[i]

def gen():
    p=10007; q=10009
    n=p*q; phi=(p-1)*(q-1)
    e=65537
    if phi%e==0: e=17
    d=pow(e,-1,phi)
    return e,d,n

def enc(msg,e,n):
    out=[]
    for ch in msg.upper():
        if ch in A:
            m=L2I(ch)
            out.append(pow(m,e,n))
        else:
            out.append(None)
    return out

def dec(c,d,n):
    out=[]
    for x in c:
        if x is None: out.append('?')
        else: out.append(I2L(pow(x,d,n)))
    return ''.join(out)

def attack(c,e,n):
    table={}
    for m in range(26):
        table[pow(m,e,n)] = m
    out=[]
    for x in c:
        if x is None: out.append('?')
        else: out.append(I2L(table[x]))
    return ''.join(out)

e,d,n = gen()
msg = "HELLO WORLD"
c = enc(msg,e,n)
print("Cipher:", c)
print("Bob decrypts:", dec(c,d,n))
print("Attacker recovers:", attack(c,e,n))
#output
Cipher: [50837557, 49384228, 37220916, 37220916, 79978083, None, 17548935, 79978083, 37220916, 14904002, 49384228]
Bob decrypts: HELLO?WORLD
Attacker recovers: HELLO?WORLD

