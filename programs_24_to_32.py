"""
Author: Dhiva
Programs 24-32: Public Key Cryptography and Digital Signatures
"""

import hashlib
import random

def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes(n: int):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0 and is_prime(i) and is_prime(n // i):
            return i, n // i
    return None, None

def extended_gcd(a: int, b: int):
    if a == 0:
        return b, 0, 1
    gcd_val, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd_val, x, y

def mod_inverse(a: int, m: int) -> int:
    _, x, _ = extended_gcd(a, m)
    return (x % m + m) % m

def rsa_encrypt(message: int, e: int, n: int) -> int:
    return pow(message, e, n)

def rsa_decrypt(ciphertext: int, d: int, n: int) -> int:
    return pow(ciphertext, d, n)

if __name__ == "__main__":
    print("="*70)
    print("PROGRAMS 24-32: PUBLIC KEY CRYPTOGRAPHY")
    print("Author: Dhiva")
    print("="*70)
    
    print("\n" + "="*70)
    print("PROGRAM 24: RSA PRIVATE KEY RECOVERY")
    print("="*70)
    
    e24 = 31
    n24 = 3599
    
    print(f"\nGiven public key: e = {e24}, n = {n24}")
    print("\nStep 1: Factor n")
    
    p24, q24 = find_primes(n24)
    print(f"Trying factors... p = {p24}, q = {q24}")
    print(f"Verification: {p24} × {q24} = {p24 * q24}")
    
    print("\nStep 2: Calculate φ(n)")
    phi_n = (p24 - 1) * (q24 - 1)
    print(f"φ(n) = (p-1)(q-1) = ({p24}-1)({q24}-1) = {phi_n}")
    
    print("\nStep 3: Find d using Extended Euclidean Algorithm")
    print(f"Need: d × e ≡ 1 (mod φ(n))")
    print(f"      d × {e24} ≡ 1 (mod {phi_n})")
    
    d24 = mod_inverse(e24, phi_n)
    print(f"\nPrivate key d = {d24}")
    
    print(f"\nVerification: ({e24} × {d24}) mod {phi_n} = {(e24 * d24) % phi_n}")
    
    msg24 = 123
    enc24 = rsa_encrypt(msg24, e24, n24)
    dec24 = rsa_decrypt(enc24, d24, n24)
    
    print(f"\nTest encryption:")
    print(f"Message:    {msg24}")
    print(f"Encrypted:  {enc24}")
    print(f"Decrypted:  {dec24}")
    
    print("\n" + "="*70)
    print("PROGRAM 25: RSA COMMON FACTOR ATTACK")
    print("="*70)
    
    n25 = 3599
    plaintext_factor = 59
    
    print(f"\nScenario: n = {n25}")
    print(f"One plaintext block shares factor with n")
    print(f"Common factor = {plaintext_factor}")
    
    p25 = gcd(n25, plaintext_factor)
    if p25 > 1:
        q25 = n25 // p25
        print(f"\nUsing gcd(n, plaintext) = gcd({n25}, {plaintext_factor}) = {p25}")
        print(f"Therefore: p = {p25}, q = {q25}")
        print(f"\n✗ RSA BROKEN! Can now compute private key!")
        
        phi25 = (p25 - 1) * (q25 - 1)
        print(f"φ(n) = {phi25}")
        print("\nThis is why plaintexts must be coprime with n")
    
    print("\n" + "="*70)
    print("PROGRAM 26: RSA KEY REUSE DANGER")
    print("="*70)
    
    print("\nScenario: Bob's private key d1 leaked")
    print("Can Bob safely generate new (e2, d2) with same n?")
    print("\n" + "-"*70)
    print("ANSWER: NO - Very unsafe!")
    print("-"*70)
    
    print("\nWhy unsafe:")
    print("1. From leaked d1 and public e1:")
    print("   Attacker can compute φ(n) = (e1 × d1 - 1) / k")
    print("\n2. With φ(n), attacker can compute d2 from any e2:")
    print("   d2 = e2^(-1) mod φ(n)")
    print("\n3. Even knowing just n is dangerous")
    
    print("\nSolution:")
    print("✓ Generate completely new n (new p and q)")
    print("✓ Never reuse modulus after key compromise")
    
    print("\n" + "="*70)
    print("PROGRAM 27: CHARACTER-BY-CHARACTER RSA")
    print("="*70)
    
    print("\nScenario: Encrypt A=0, B=1, ..., Z=25 separately")
    print("\n" + "-"*70)
    print("ANSWER: Completely insecure!")
    print("-"*70)
    
    message27 = "HELLO"
    e27 = 31
    n27 = 3599
    
    print(f"\nMessage: {message27}")
    print(f"\nCharacter-by-character encryption:")
    
    lookup_table = {}
    for char in message27:
        val = ord(char) - 65
        enc = rsa_encrypt(val, e27, n27)
        lookup_table[val] = enc
        print(f"  {char} ({val:2d}) → {enc:4d}")
    
    print("\nAttack:")
    print("1. Only 26 possible plaintexts")
    print("2. Precompute all 26 encryptions")
    print("3. Build lookup table")
    print("4. Instant decryption!")
    
    print("\nPrecomputed lookup table:")
    for i in range(26):
        enc = rsa_encrypt(i, e27, n27)
        char = chr(i + 65)
        print(f"  {enc:4d} → {char}", end="   ")
        if (i + 1) % 5 == 0:
            print()
    
    print("\n\nDefense: Use proper padding (OAEP) and larger blocks")
    
    print("\n" + "="*70)
    print("PROGRAM 28: DIFFIE-HELLMAN KEY EXCHANGE")
    print("="*70)
    
    p28 = 23
    g28 = 5
    alice_private = 6
    bob_private = 15
    
    print(f"\nPublic parameters:")
    print(f"  Prime p = {p28}")
    print(f"  Generator g = {g28}")
    
    alice_public = pow(g28, alice_private, p28)
    bob_public = pow(g28, bob_private, p28)
    
    print(f"\nAlice:")
    print(f"  Private key a = {alice_private}")
    print(f"  Public key A = g^a mod p = {g28}^{alice_private} mod {p28} = {alice_public}")
    
    print(f"\nBob:")
    print(f"  Private key b = {bob_private}")
    print(f"  Public key B = g^b mod p = {g28}^{bob_private} mod {p28} = {bob_public}")
    
    alice_shared = pow(bob_public, alice_private, p28)
    bob_shared = pow(alice_public, bob_private, p28)
    
    print(f"\nShared secret computation:")
    print(f"  Alice: B^a mod p = {bob_public}^{alice_private} mod {p28} = {alice_shared}")
    print(f"  Bob:   A^b mod p = {alice_public}^{bob_private} mod {p28} = {bob_shared}")
    print(f"\nShared secret established: {alice_shared == bob_shared}")
    
    print("\n" + "-"*70)
    print("Alternative: What if they sent x^a instead of a^x?")
    print("-"*70)
    print("Problem: Eve can compute gcd(x^a, x^b) = x^gcd(a,b)")
    print("This leaks information about private keys!")
    print("Not secure!")
    
    print("\n" + "="*70)
    print("PROGRAM 29: SHA-3 LANE PROPAGATION")
    print("="*70)
    
    print("\nSHA-3 with 1024-bit blocks:")
    print(f"  Block size: 1024 bits")
    print(f"  Lane size: 64 bits")
    print(f"  Total lanes: 1024/64 = 16 lanes")
    print(f"  Capacity lanes: 8 (initially zero)")
    
    print("\nAfter first absorption:")
    print("  All capacity lanes get mixed with message")
    print("  Rounds needed for all to be nonzero: 1")
    
    print("\nReason: SHA-3's permutation function (Keccak-f)")
    print("spreads bits across all lanes in single round")
    
    print("\n" + "="*70)
    print("PROGRAM 30: CBC-MAC VULNERABILITY")
    print("="*70)
    
    print("\nScenario:")
    print("  Message X, MAC T = MAC(K, X)")
    print("\nVulnerability:")
    print("  Attacker can forge MAC for: X || (X ⊕ T)")
    
    print("\nWhy:")
    print("  CBC-MAC(X || Y) = E(E(X) ⊕ Y)")
    print("  If Y = X ⊕ T, then:")
    print("  MAC(X || (X⊕T)) = E(T ⊕ (X⊕T)) = E(X) = T")
    
    print("\nDefense: Use CMAC with message length encoding")
    
    print("\n" + "="*70)
    print("PROGRAM 31: CMAC SUBKEY GENERATION")
    print("="*70)
    
    print("\nConstants for CMAC:")
    print("  64-bit blocks:  Rb = 0x1B")
    print("  128-bit blocks: Rb = 0x87")
    
    print("\nSubkey generation:")
    print("1. L = E(K, 0^blocksize)")
    print("2. If MSB(L) = 0: K1 = L << 1")
    print("   If MSB(L) = 1: K1 = (L << 1) ⊕ Rb")
    print("3. If MSB(K1) = 0: K2 = K1 << 1")
    print("   If MSB(K1) = 1: K2 = (K1 << 1) ⊕ Rb")
    
    print("\nPurpose:")
    print("- Ensure different processing for last block")
    print("- Prevent length extension attacks")
    print("- K1 for complete final block")
    print("- K2 for incomplete final block")
    
    print("\n" + "="*70)
    print("PROGRAM 32: DSA VS RSA SIGNATURES")
    print("="*70)
    
    p32 = 23
    q32 = 11
    g32 = 2
    private32 = 5
    message32 = "HELLO"
    
    print("\nDSA Signature Generation:")
    k32 = random.randint(1, q32-1)
    r32 = pow(g32, k32, p32) % q32
    h32 = int(hashlib.sha256(message32.encode()).hexdigest(), 16) % q32
    
    k_inv = mod_inverse(k32, q32)
    s32 = (k_inv * (h32 + private32 * r32)) % q32
    
    print(f"Message: {message32}")
    print(f"Random k: {k32}")
    print(f"Signature (r, s): ({r32}, {s32})")
    
    print("\nKey difference:")
    print("-" * 70)
    print("DSA:")
    print("  • New random k for each signature")
    print("  • Same message → different signatures")
    print("  • k must be secret and unpredictable")
    
    print("\nRSA:")
    print("  • Deterministic")
    print("  • Same message → same signature")
    print("  • No randomness needed")
    
    print("\nImplications:")
    print("  ✓ DSA: More secure against some attacks")
    print("  ✗ DSA: Bad k reveals private key!")
    print("  ✓ RSA: Simpler implementation")
    print("  ✓ RSA: Signature verifiable offline")
    
    print("\n" + "="*70)