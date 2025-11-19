from collections import Counter

# English letter frequency (most common to least)
english_freq_order = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

def frequency_attack(ciphertext):
    # Count frequency of letters in ciphertext
    counter = Counter(c for c in ciphertext.upper() if c.isalpha())
    sorted_cipher_letters = [item[0] for item in counter.most_common()]
    
    # Map most frequent cipher letters to English frequency order
    mapping = dict(zip(sorted_cipher_letters, english_freq_order))
    
    # Decrypt using frequency mapping
    decrypted = ''
    for char in ciphertext.upper():
        if char.isalpha():
            decrypted += mapping.get(char, '?')
        else:
            decrypted += char
    return decrypted

def demo():
    ciphertext = "ZEBBWKXKZOBYOBZEXKXKBOB"
    print("🔒 Ciphertext:", ciphertext)
    guessed_plaintext = frequency_attack(ciphertext)
    print("🔓 Guessed Plaintext:", guessed_plaintext)

if __name__ == "__main__":
    demo()
#output
🔒 Ciphertext: ZEBBWKXKZOBYOBZEXKXKBOB
🔓 Guessed Plaintext: ETTTOHSHETRNERETOHSHRER



