"""
Author: Dhiva
Program 16: Frequency Attack on Monoalphabetic Substitution
"""

from collections import Counter
import random
import string

def calculate_fitness(text: str) -> float:
    english_freq = {
        'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97,
        'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25,
        'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36,
        'F': 2.23, 'G': 2.02, 'Y': 1.97, 'P': 1.93, 'B': 1.29,
        'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z': 0.07
    }
    
    text = text.upper()
    letters = [c for c in text if c.isalpha()]
    if len(letters) == 0:
        return -999999
    
    freq_count = Counter(letters)
    total = len(letters)
    
    score = 0
    for letter in string.ascii_uppercase:
        actual_freq = (freq_count.get(letter, 0) / total) * 100
        expected_freq = english_freq.get(letter, 0)
        score -= abs(actual_freq - expected_freq)
    
    return score

def monoalphabetic_decrypt(ciphertext: str, key: dict) -> str:
    result = ""
    for char in ciphertext:
        if char.upper() in key:
            decrypted_char = key[char.upper()]
            result += decrypted_char if char.isupper() else decrypted_char.lower()
        else:
            result += char
    return result

def create_initial_key(ciphertext: str) -> dict:
    cipher_freq = Counter(c.upper() for c in ciphertext if c.isalpha())
    english_order = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
    
    sorted_cipher = [item[0] for item in cipher_freq.most_common()]
    
    key = {}
    for i, cipher_char in enumerate(sorted_cipher):
        if i < len(english_order):
            key[cipher_char] = english_order[i]
    
    for char in string.ascii_uppercase:
        if char not in key:
            for plain_char in string.ascii_uppercase:
                if plain_char not in key.values():
                    key[char] = plain_char
                    break
    
    return key

def hill_climbing_attack(ciphertext: str, iterations: int = 1000) -> tuple:
    best_key = create_initial_key(ciphertext)
    best_text = monoalphabetic_decrypt(ciphertext, best_key)
    best_score = calculate_fitness(best_text)
    
    for _ in range(iterations):
        new_key = best_key.copy()
        
        chars = list(new_key.keys())
        i, j = random.sample(range(len(chars)), 2)
        new_key[chars[i]], new_key[chars[j]] = new_key[chars[j]], new_key[chars[i]]
        
        new_text = monoalphabetic_decrypt(ciphertext, new_key)
        new_score = calculate_fitness(new_text)
        
        if new_score > best_score:
            best_key = new_key
            best_text = new_text
            best_score = new_score
    
    return best_key, best_text, best_score

if __name__ == "__main__":
    print("="*70)
    print("PROGRAM 16: FREQUENCY ATTACK ON MONOALPHABETIC CIPHER")
    print("Author: Dhiva")
    print("="*70)
    
    print("\nMonoalphabetic Substitution:")
    print("-" * 70)
    print("Each letter is consistently replaced with another letter.")
    print("Key space: 26! ≈ 4×10²⁶ possible keys")
    print("Too large for brute force, but vulnerable to frequency analysis!")
    
    original_key = "QWERTYUIOPASDFGHJKLZXCVBNM"
    plaintext = """THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG
CRYPTOGRAPHY IS THE ART OF WRITING OR SOLVING CODES
FREQUENCY ANALYSIS CAN BREAK SUBSTITUTION CIPHERS"""
    
    cipher_alphabet = string.ascii_uppercase
    plain_to_cipher = {cipher_alphabet[i]: original_key[i] for i in range(26)}
    
    ciphertext = ""
    for char in plaintext:
        if char.upper() in plain_to_cipher:
            encrypted_char = plain_to_cipher[char.upper()]
            ciphertext += encrypted_char if char.isupper() else encrypted_char.lower()
        else:
            ciphertext += char
    
    print("\n" + "="*70)
    print("ORIGINAL MESSAGE")
    print("="*70)
    print(plaintext)
    
    print("\n" + "="*70)
    print("ENCRYPTED MESSAGE")
    print("="*70)
    print(ciphertext)
    
    print("\n" + "="*70)
    print("FREQUENCY ANALYSIS")
    print("="*70)
    
    cipher_letters = [c.upper() for c in ciphertext if c.isalpha()]
    cipher_freq = Counter(cipher_letters)
    total = len(cipher_letters)
    
    print(f"\nTotal letters: {total}")
    print("\nMost frequent letters in ciphertext:")
    for letter, count in cipher_freq.most_common(15):
        percentage = (count / total) * 100
        bar = '█' * int(percentage * 2)
        print(f"{letter}: {count:3d} ({percentage:5.2f}%) {bar}")
    
    print("\n" + "="*70)
    print("AUTOMATED ATTACK - METHOD 1: Frequency Mapping")
    print("="*70)
    
    initial_key = create_initial_key(ciphertext)
    
    print("\nInitial key guess (based on frequency):")
    print("Cipher -> Plain")
    for cipher_char, plain_char in sorted(initial_key.items())[:13]:
        print(f"  {cipher_char} -> {plain_char}", end="   ")
    print()
    for cipher_char, plain_char in sorted(initial_key.items())[13:]:
        print(f"  {cipher_char} -> {plain_char}", end="   ")
    print()
    
    initial_decrypt = monoalphabetic_decrypt(ciphertext, initial_key)
    initial_score = calculate_fitness(initial_decrypt)
    
    print(f"\nInitial decryption (first 100 chars):")
    print(initial_decrypt[:100] + "...")
    print(f"Fitness score: {initial_score:.2f}")
    
    print("\n" + "="*70)
    print("AUTOMATED ATTACK - METHOD 2: Hill Climbing")
    print("="*70)
    
    print("\nApplying hill climbing optimization...")
    print("Testing thousands of key variations...")
    
    best_key, best_text, best_score = hill_climbing_attack(ciphertext, iterations=2000)
    
    print(f"\nOptimized fitness score: {best_score:.2f}")
    print(f"Improvement: {best_score - initial_score:.2f}")
    
    print("\n" + "="*70)
    print("BEST DECRYPTION FOUND")
    print("="*70)
    print(best_text)
    
    print("\n" + "="*70)
    print("TOP 10 POSSIBLE PLAINTEXTS")
    print("="*70)
    
    results = []
    for attempt in range(10):
        key, text, score = hill_climbing_attack(ciphertext, iterations=1000)
        results.append((score, text, key))
    
    results.sort(reverse=True)
    
    for rank, (score, text, key) in enumerate(results, 1):
        print(f"\n{rank}. Score: {score:.2f}")
        print(f"   {text[:80]}...")
    
    print("\n" + "="*70)
    print("ATTACK ANALYSIS")
    print("="*70)
    
    print("\nWhy this works:")
    print("1. English letter frequencies are predictable")
    print("2. Common bigrams: TH, HE, IN, ER, AN")
    print("3. Common trigrams: THE, AND, ING, ION")
    print("4. Pattern recognition helps refine guesses")
    
    print("\nLimitations:")
    print("1. Requires sufficient ciphertext (50+ letters)")
    print("2. Short messages are harder to break")
    print("3. May produce multiple plausible decryptions")
    print("4. Manual refinement often needed")
    
    print("\n" + "="*70)
    print("DEFENSE MECHANISMS")
    print("="*70)
    
    print("\n1. Use polyalphabetic ciphers (Vigenère)")
    print("2. Use modern encryption (AES)")
    print("3. Add homophonic substitution")
    print("4. Combine with transposition")
    
    print("\n" + "="*70)