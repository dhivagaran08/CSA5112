"""
Author: Dhiva
Programs 18-23: DES Analysis and Block Cipher Modes
"""

def xor_bytes(a: bytes, b: bytes) -> bytes:
    return bytes(x ^ y for x, y in zip(a, b))

def simple_encrypt(block: bytes, key: bytes) -> bytes:
    return xor_bytes(block, key)

def ecb_encrypt(plaintext: bytes, key: bytes, block_size: int = 8) -> bytes:
    ciphertext = b''
    for i in range(0, len(plaintext), block_size):
        block = plaintext[i:i+block_size]
        if len(block) < block_size:
            block = block + b'\x00' * (block_size - len(block))
        encrypted = simple_encrypt(block, key[:block_size])
        ciphertext += encrypted
    return ciphertext

def cbc_encrypt(plaintext: bytes, key: bytes, iv: bytes, block_size: int = 8) -> bytes:
    ciphertext = b''
    prev_block = iv
    for i in range(0, len(plaintext), block_size):
        block = plaintext[i:i+block_size]
        if len(block) < block_size:
            block = block + b'\x00' * (block_size - len(block))
        xored = xor_bytes(block, prev_block)
        encrypted = simple_encrypt(xored, key[:block_size])
        ciphertext += encrypted
        prev_block = encrypted
    return ciphertext

def cbc_decrypt(ciphertext: bytes, key: bytes, iv: bytes, block_size: int = 8) -> bytes:
    plaintext = b''
    prev_block = iv
    for i in range(0, len(ciphertext), block_size):
        block = ciphertext[i:i+block_size]
        decrypted = simple_encrypt(block, key[:block_size])
        plaintext_block = xor_bytes(decrypted, prev_block)
        plaintext += plaintext_block
        prev_block = block
    return plaintext

def counter_mode(data: bytes, key: bytes, counter: int, block_size: int = 8) -> bytes:
    result = b''
    for i in range(0, len(data), block_size):
        block = data[i:i+block_size]
        counter_bytes = counter.to_bytes(block_size, 'big')
        keystream = simple_encrypt(counter_bytes, key[:block_size])
        encrypted = xor_bytes(block, keystream[:len(block)])
        result += encrypted
        counter += 1
    return result

if __name__ == "__main__":
    print("="*70)
    print("PROGRAMS 18-23: BLOCK CIPHER MODES")
    print("Author: Dhiva")
    print("="*70)
    
    print("\n" + "="*70)
    print("PROGRAM 18: DES SUBKEY ANALYSIS")
    print("="*70)
    
    print("\nDES Subkey Structure:")
    print("-" * 70)
    print("Initial 56-bit key split into C0 (28 bits) and D0 (28 bits)")
    print("\nFor each round:")
    print("- First 24 bits of subkey come from permutation of C")
    print("- Second 24 bits come from permutation of D")
    print("- C and D are disjoint subsets")
    
    print("\nPermuted Choice 2 (PC-2) selects 48 bits from 56:")
    print("Bits 1-24:  From C (left half)")
    print("Bits 25-48: From D (right half)")
    
    print("\n" + "="*70)
    print("PROGRAM 19: CBC MODE ENCRYPTION")
    print("="*70)
    
    plaintext19 = b"HELLO WORLD!!!!!"
    key19 = b"SECRETKEY"
    iv19 = b"INITVECT"
    
    print(f"\nPlaintext: {plaintext19}")
    print(f"Key: {key19}")
    print(f"IV: {iv19}")
    
    cbc_cipher = cbc_encrypt(plaintext19, key19, iv19)
    cbc_plain = cbc_decrypt(cbc_cipher, key19, iv19)
    
    print(f"\nCBC Encrypted: {cbc_cipher.hex()}")
    print(f"CBC Decrypted: {cbc_plain}")
    
    print("\nSecurity vs Performance:")
    print("For security: CBC mode (each block depends on previous)")
    print("For performance: ECB mode (parallel processing possible)")
    
    print("\n" + "="*70)
    print("PROGRAM 20: ERROR PROPAGATION ANALYSIS")
    print("="*70)
    
    print("\nECB Mode Error Propagation:")
    print("-" * 70)
    print("Error in C1 affects: Only P1")
    print("Blocks beyond P1: NOT affected")
    print("\nReason: Each block encrypted independently")
    
    print("\nCBC Mode Error Propagation:")
    print("-" * 70)
    print("Error in transmitted C1:")
    print("  - Corrupts P1 (directly)")
    print("  - Corrupts P2 (C1 used as IV for P2)")
    print("  - P3 onwards: NOT affected")
    
    print("\nBit error in source P1:")
    print("  - Propagates to: C1 only")
    print("  - Effect at receiver: P1 has error, C2 affected")
    print("  - P3 onwards: Clean")
    
    test_plain20 = b"BLOCK1" + b"BLOCK2" + b"BLOCK3"
    test_key20 = b"KEY12345"
    test_iv20 = b"IV123456"
    
    cbc_test = cbc_encrypt(test_plain20, test_key20, test_iv20, 6)
    
    print(f"\nOriginal: {cbc_test.hex()}")
    
    corrupted = bytearray(cbc_test)
    corrupted[0] ^= 0x01
    
    cbc_corrupted = cbc_decrypt(bytes(corrupted), test_key20, test_iv20, 6)
    
    print(f"After error in C1: {cbc_corrupted}")
    print("Notice: First two blocks affected, third block clean")
    
    print("\n" + "="*70)
    print("PROGRAM 21: PADDING EXPLANATION")
    print("="*70)
    
    print("\nPadding scheme: 1 bit followed by 0 bits")
    print("\nWhy pad even complete blocks?")
    print("-" * 70)
    print("1. Unambiguous padding removal")
    print("   - Receiver always knows to remove padding")
    print("   - No confusion about whether last block had padding")
    print("\n2. Security consideration")
    print("   - Prevents padding oracle attacks")
    print("   - Makes all messages follow same pattern")
    print("\n3. Protocol reliability")
    print("   - Standardized behavior")
    print("   - Easier to implement correctly")
    
    msg_complete = b"12345678"
    msg_partial = b"12345"
    
    print(f"\nExample 1: Complete block (8 bytes)")
    print(f"Message: {msg_complete} (length {len(msg_complete)})")
    print(f"Padded:  {msg_complete + b'\\x80' + b'\\x00'*7}")
    print(f"         (added full padding block)")
    
    print(f"\nExample 2: Partial block (5 bytes)")
    print(f"Message: {msg_partial} (length {len(msg_partial)})")
    print(f"Padded:  {msg_partial + b'\\x80' + b'\\x00'*2}")
    print(f"         (padded to 8 bytes)")
    
    print("\n" + "="*70)
    print("PROGRAM 22: S-DES CBC MODE")
    print("="*70)
    
    plain22 = bytes([0b00000001, 0b00100011])
    key22 = bytes([0b01111111, 0b01000000])
    iv22 = bytes([0b10101010])
    
    print(f"Plaintext (binary):  {' '.join(format(b, '08b') for b in plain22)}")
    print(f"Key (binary):        0111111101")
    print(f"IV (binary):         {format(iv22[0], '08b')}")
    
    enc22 = cbc_encrypt(plain22, key22, iv22, 1)
    
    print(f"Encrypted (binary):  {' '.join(format(b, '08b') for b in enc22)}")
    print(f"Expected:            11110100 00001011")
    
    print("\n" + "="*70)
    print("PROGRAM 23: COUNTER MODE")
    print("="*70)
    
    plain23 = bytes([0b00000001, 0b00000010, 0b00000100])
    key23 = bytes([0b01111111, 0b01000000])
    counter23 = 0
    
    print(f"Plaintext (binary): {' '.join(format(b, '08b') for b in plain23)}")
    print(f"Key (binary):       0111111101")
    print(f"Counter start:      {counter23}")
    
    enc23 = counter_mode(plain23, key23, counter23, 1)
    dec23 = counter_mode(enc23, key23, counter23, 1)
    
    print(f"\nEncrypted (binary): {' '.join(format(b, '08b') for b in enc23)}")
    print(f"Expected:           00111000 01001111 00110010")
    print(f"\nDecrypted (binary): {' '.join(format(b, '08b') for b in dec23)}")
    print(f"Match: {plain23 == dec23}")
    
    print("\n" + "="*70)
    print("BLOCK CIPHER MODES COMPARISON")
    print("="*70)
    
    print("\nECB (Electronic Codebook):")
    print("  ✓ Parallel processing")
    print("  ✓ Random access")
    print("  ✗ Identical blocks → identical ciphertext")
    print("  ✗ Not recommended")
    
    print("\nCBC (Cipher Block Chaining):")
    print("  ✓ Each block depends on previous")
    print("  ✓ Good diffusion")
    print("  ✗ Sequential encryption")
    print("  ✓ Most common mode")
    
    print("\nCTR (Counter):")
    print("  ✓ Parallel processing")
    print("  ✓ Random access")
    print("  ✓ No padding needed")
    print("  ✓ Modern choice")
    
    print("\n" + "="*70)