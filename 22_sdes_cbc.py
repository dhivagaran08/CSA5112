IV = '10101010'

P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
P8  = [6, 3, 7, 4, 8, 5, 10, 9]
IP  = [2, 6, 3, 1, 4, 8, 5, 7]
IP_INV = [4, 1, 3, 5, 7, 2, 8, 6]
EP  = [4, 1, 2, 3, 2, 3, 4, 1]
P4  = [2, 4, 3, 1]

S0 = [[[1,0],[0,1],[3,2],[2,3]],
      [[3,2],[1,0],[0,1],[2,3]]]

S1 = [[[0,1],[2,0],[1,3],[3,2]],
      [[2,0],[1,3],[3,2],[0,1]]]

def permute(bits, table):
    return ''.join(bits[i-1] for i in table)

def left_shift(bits, n):
    return bits[n:] + bits[:n]

def xor(a, b):
    return ''.join('0' if i == j else '1' for i, j in zip(a, b))

def sbox(bits, box):
    row = int(bits[0] + bits[3], 2)
    col = int(bits[1] + bits[2], 2)
    return format(box[row][col], '02b')

def fk(bits, key):
    L, R = bits[:4], bits[4:]
    temp = permute(R, EP)
    temp = xor(temp, key)
    left, right = temp[:4], temp[4:]
    s_out = sbox(left, S0) + sbox(right, S1)
    s_out = permute(s_out, P4)
    return xor(L, s_out) + R

def encrypt_block(plain, k1, k2):
    bits = permute(plain, IP)
    bits = fk(bits, k1)
    bits = bits[4:] + bits[:4]
    bits = fk(bits, k2)
    return permute(bits, IP_INV)

def generate_keys(key):
    key = permute(key, P10)
    L, R = key[:5], key[5:]
    Ls1, Rs1 = left_shift(L, 1), left_shift(R, 1)
    k1 = permute(Ls1 + Rs1, P8)
    Ls2, Rs2 = left_shift(Ls1, 2), left_shift(Rs1, 2)
    k2 = permute(Ls2 + Rs2, P8)
    return k1, k2

def cbc_encrypt(plaintext_blocks, key, iv):
    k1, k2 = generate_keys(key)
    prev = iv
    ciphertext = []
    for block in plaintext_blocks:
        block = xor(block, prev)
        enc = encrypt_block(block, k1, k2)
        ciphertext.append(enc)
        prev = enc
    return ciphertext

key = '1010000010'
plaintext_blocks = ['11010111', '00110011']
ciphertext = cbc_encrypt(plaintext_blocks, key, IV)

for i, c in enumerate(ciphertext, 1):
    print(f"Block {i}: {c}")
#output
Block 1: 00010100
Block 2: 10101100



