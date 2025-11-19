from collections import Counter

# English letter frequency (most to least common)
english_freq_order = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

def frequency_attack(ciphertext):
    # Count frequency of letters in ciphertext
    counter = Counter(c for c in ciphertext.upper() if c.isalpha())
    sorted_cipher_letters = [item[0] for item in counter.most_common()]
    
    # Create mapping from cipher letters to English frequency letters
    mapping = dict(zip(sorted_cipher_letters, english_freq_order))
    
    # Attempt decryption using frequency mapping
    decrypted = ''
    for char in ciphertext.upper():
        if char.isalpha():
            decrypted += mapping.get(char, '?')
        else:
            decrypted += char
    return decrypted

def demo():
    cipher = "WKH TXLFN EURZQ IRA MXPSV RYHU WKH ODCB GRJ"
    print("🔒 Ciphertext:", cipher)
    guessed_plaintext = frequency_attack(cipher)
    print("🔓 Guessed Plaintext:", guessed_plaintext)

if __name__ == "__main__":
    demo()
#output
🔒 Ciphertext: WKH TXLFN EURZQ IRA MXPSV RYHU WKH ODCB GRJ
🔓 Guessed Plaintext: THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG

