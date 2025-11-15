"""
Author: Dhiva
Program 17: DES Key Generation for Decryption
"""

def left_rotate(bits: str, n: int) -> str:
    return bits[n:] + bits[:n]

def right_rotate(bits: str, n: int) -> str:
    return bits[-n:] + bits[:-n]

def generate_encryption_keys(initial_key: str) -> list:
    shift_schedule = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    
    C = initial_key[:28]
    D = initial_key[28:56]
    
    keys = []
    
    for round_num in range(16):
        C = left_rotate(C, shift_schedule[round_num])
        D = left_rotate(D, shift_schedule[round_num])
        
        combined = C + D
        subkey = combined[:48]
        keys.append(subkey)
    
    return keys

def generate_decryption_keys(initial_key: str) -> list:
    encryption_keys = generate_encryption_keys(initial_key)
    return encryption_keys[::-1]

if __name__ == "__main__":
    print("="*70)
    print("PROGRAM 17: DES KEY GENERATION FOR DECRYPTION")
    print("Author: Dhiva")
    print("="*70)
    
    print("\nDES (Data Encryption Standard):")
    print("-" * 70)
    print("Block size: 64 bits")
    print("Key size: 56 bits (64 with parity)")
    print("Rounds: 16")
    print("Structure: Feistel network")
    
    initial_key = "01010101" * 7
    
    print("\n" + "="*70)
    print("KEY GENERATION SCHEDULE")
    print("="*70)
    
    print(f"\nInitial 56-bit key:")
    print(f"{initial_key[:28]} (C0)")
    print(f"{initial_key[28:]} (D0)")
    
    print("\n" + "="*70)
    print("ENCRYPTION KEY SCHEDULE")
    print("="*70)
    
    shift_schedule = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    
    print("\nShift schedule for encryption:")
    print("Round | Shift")
    print("-" * 20)
    for i, shift in enumerate(shift_schedule, 1):
        print(f"  {i:2d}  |   {shift}")
    
    encryption_keys = generate_encryption_keys(initial_key)
    
    print("\n" + "="*70)
    print("ENCRYPTION SUBKEYS (K1 to K16)")
    print("="*70)
    
    for i, key in enumerate(encryption_keys, 1):
        print(f"K{i:2d}: {key[:24]}...{key[24:48]}")
    
    print("\n" + "="*70)
    print("DECRYPTION KEY SCHEDULE")
    print("="*70)
    
    print("\nFor decryption, use keys in REVERSE order:")
    print("Decryption uses: K16, K15, K14, ..., K2, K1")
    
    decryption_keys = generate_decryption_keys(initial_key)
    
    print("\n" + "="*70)
    print("DECRYPTION SUBKEYS (K16 to K1)")
    print("="*70)
    
    for i, key in enumerate(decryption_keys, 1):
        print(f"Round {i:2d} uses K{17-i:2d}: {key[:24]}...{key[24:48]}")
    
    print("\n" + "="*70)
    print("SHIFT SCHEDULE FOR DECRYPTION")
    print("="*70)
    
    print("\nOption 1: Use encryption keys in reverse")
    print("Round | Encryption Key | Decryption Key")
    print("-" * 45)
    for i in range(16):
        enc_round = i + 1
        dec_round = 16 - i
        print(f"  {enc_round:2d}  |      K{enc_round:2d}        |      K{dec_round:2d}")
    
    print("\n" + "="*70)
    print("VERIFICATION")
    print("="*70)
    
    print("\nVerifying key reversal:")
    for i in range(5):
        enc_key = encryption_keys[i][:16]
        dec_key = decryption_keys[15-i][:16]
        match = "✓" if enc_key == dec_key else "✗"
        print(f"Enc K{i+1} == Dec K{16-i}: {match}")
    
    print("\n" + "="*70)
    print("WHY REVERSE ORDER WORKS")
    print("="*70)
    
    print("\nFeistel Structure Property:")
    print("1. Encryption: E(P) = L16R16 where")
    print("   - L16 = R15")
    print("   - R16 = L15 ⊕ f(R15, K16)")
    print("\n2. Decryption: Apply same operations with reversed keys")
    print("   - First round uses K16")
    print("   - Last round uses K1")
    print("\n3. This 'undoes' the encryption step by step")
    
    print("\n" + "="*70)
    print("IMPLEMENTATION NOTE")
    print("="*70)
    
    print("\nIn practice:")
    print("- Generate all 16 keys once")
    print("- For encryption: use keys[0] to keys[15]")
    print("- For decryption: use keys[15] to keys[0]")
    print("- Same algorithm, just reversed key order")
    
    print("\n" + "="*70)