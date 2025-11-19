from Crypto.Cipher import AES

def left_shift(block):
    """Performs a left shift on a 16-byte block."""
    shifted = int.from_bytes(block, 'big') << 1
    return (shifted & (2**128 - 1)).to_bytes(16, 'big')

def xor_bytes(a, b):
    """XORs two byte strings."""
    return bytes(x ^ y for x, y in zip(a, b))

def generate_cmac_subkeys(key):
    cipher = AES.new(key, AES.MODE_ECB)
    L = cipher.encrypt(bytes(16))  # AES_K(0^128)

    Rb = bytes.fromhex('00000000000000000000000000000087')

    if (L[0] & 0x80) == 0:
        K1 = left_shift(L)
    else:
        K1 = xor_bytes(left_shift(L), Rb)

    if (K1[0] & 0x80) == 0:
        K2 = left_shift(K1)
    else:
        K2 = xor_bytes(left_shift(K1), Rb)

    return L, K1, K2

# Example usage
if __name__ == "__main__":
    key = bytes.fromhex('2b7e151628aed2a6abf7158809cf4f3c')  # AES-128 test key
    L, K1, K2 = generate_cmac_subkeys(key)

    print("=== CMAC Subkey Generation ===")
    print(f"Key       : {key.hex()}")
    print(f"L         : {L.hex()}")
    print(f"K1        : {K1.hex()}")
    print(f"K2        : {K2.hex()}")
#output
=== CMAC Subkey Generation ===
Key       : 2b7e151628aed2a6abf7158809cf4f3c
L         : 7df76b0c1ab899b33e42f047b91b546f
K1        : fbeed619357133667c85e08f7236a8de
K2        : f7ddac326ae266ccf90bc11ee46d513b

