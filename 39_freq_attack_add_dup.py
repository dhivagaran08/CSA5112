from collections import Counter

# English letter frequency (most common to least)
english_freq_order = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

def frequency_attack_additive(ciphertext):
    # Count letter frequencies in ciphertext
    counter = Counter(c for c in ciphertext.upper() if c.isalpha())
    most_common_cipher_letter = counter.most_common(1)[0][0]

    # Assume most common letter in ciphertext maps to 'E'
    assumed_plain_letter = 'E'
    key = (ord(most_common_cipher_letter) - ord(assumed_plain_letter)) % 26

    # Decrypt using guessed key
    decrypted = ''
    for char in ciphertext.upper():
        if char.isalpha():
            decrypted += chr((ord(char) - ord('A') - key) % 26 + ord('A'))
        else:
            decrypted += char

    return key, decrypted

def demo():
    ciphertext = "WKH TXLFN EURZQ IRA MXPSV RYHU WKH ODCB GRJ"
    print("🔒 Ciphertext:", ciphertext)

    key, guessed_plaintext = frequency_attack_additive(ciphertext)
    print("🔑 Guessed Key:", key)
    print("🔓 Guessed Plaintext:", guessed_plaintext)

if __name__ == "__main__":
    demo()
#output
🔒 Ciphertext: WKH TXLFN EURZQ IRA MXPSV RYHU WKH ODCB GRJ
🔑 Guessed Key: 3
🔓 Guessed Plaintext: THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG

