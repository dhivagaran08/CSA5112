import random
import string

def generate_key(length):
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(length))

def encrypt(message, key):
    encrypted = []
    for m, k in zip(message, key):
        enc_char = chr(((ord(m) - ord('A')) + (ord(k) - ord('A'))) % 26 + ord('A'))
        encrypted.append(enc_char)
    return ''.join(encrypted)

def decrypt(ciphertext, key):
    decrypted = []
    for c, k in zip(ciphertext, key):
        dec_char = chr(((ord(c) - ord('A')) - (ord(k) - ord('A')) + 26) % 26 + ord('A'))
        decrypted.append(dec_char)
    return ''.join(decrypted)

def otp_vigenere_demo():
    message = "HELLOWORLD"
    key = generate_key(len(message))

    print("📨 Message:", message)
    print("🔑 Key    :", key)

    ciphertext = encrypt(message, key)
    print("🔒 Encrypted:", ciphertext)

    decrypted = decrypt(ciphertext, key)
    print("🔓 Decrypted:", decrypted)

if __name__ == "__main__":
    otp_vigenere_demo()
#output
📨 Message: HELLOWORLD
🔑 Key    : QWERTYUIOPL
🔒 Encrypted: DZVZJZCZZW
🔓 Decrypted: HELLOWORLD

