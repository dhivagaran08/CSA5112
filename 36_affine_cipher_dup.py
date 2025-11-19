def mod_inverse(a, m):
    # Extended Euclidean Algorithm to find modular inverse
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError("No modular inverse exists")

def affine_encrypt(text, a, b):
    result = ''
    for char in text.upper():
        if char.isalpha():
            enc = (a * (ord(char) - ord('A')) + b) % 26
            result += chr(enc + ord('A'))
        else:
            result += char
    return result

def affine_decrypt(cipher, a, b):
    result = ''
    a_inv = mod_inverse(a, 26)
    for char in cipher.upper():
        if char.isalpha():
            dec = (a_inv * ((ord(char) - ord('A')) - b)) % 26
            result += chr(dec + ord('A'))
        else:
            result += char
    return result

def affine_demo():
    a = 5  # Must be coprime with 26
    b = 8
    message = "AFFINE CIPHER"

    print("📨 Original:", message)
    encrypted = affine_encrypt(message, a, b)
    print("🔒 Encrypted:", encrypted)
    decrypted = affine_decrypt(encrypted, a, b)
    print("🔓 Decrypted:", decrypted)

if __name__ == "__main__":
    affine_demo()
#output
📨 Original: AFFINE CIPHER
🔒 Encrypted: IHHWVCSWFRCP
🔓 Decrypted: AFFINECIPHER

