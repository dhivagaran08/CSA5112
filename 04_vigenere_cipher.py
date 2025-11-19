# Program 4: Vigenere (Polyalphabetic) Cipher
def vigenere_encrypt(plaintext, key):
    plaintext = plaintext.upper()
    key = key.upper()
    result = ""
    key_index = 0
    
    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 65
            result += chr((ord(char) - 65 + shift) % 26 + 65)
            key_index += 1
        else:
            result += char
    return result

def vigenere_decrypt(ciphertext, key):
    ciphertext = ciphertext.upper()
    key = key.upper()
    result = ""
    key_index = 0
    
    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 65
            result += chr((ord(char) - 65 - shift) % 26 + 65)
            key_index += 1
        else:
            result += char
    return result

def main():
    print("=== Vigenere Cipher ===")
    choice = input("'e' for encrypt, 'd' for decrypt: ").lower()
    text = input("Enter text: ")
    key = input("Enter key: ")
    
    if choice == 'e':
        print(f"Encrypted: {vigenere_encrypt(text, key)}")
    else:
        print(f"Decrypted: {vigenere_decrypt(text, key)}")

if __name__ == "__main__":
    main()
#output
Enter Plaintext : HELLOWORLD
Enter Key       : KEY

--- Repeated Key ---
KEYKEYKEYK

--- Encryption Process ---
H + K = R
E + E = I
L + Y = J
L + K = V
O + E = S
W + Y = U
O + K = Y
R + E = V
L + Y = J
D + K = N

--- Ciphertext ---
RIJVSUYVJN

--- Decryption Process ---
R - K = H
I - E = E
J - Y = L
V - K = L
S - E = O
U - Y = W
Y - K = O
V - E = R
J - Y = L
N - K = D

--- Decrypted Text ---
HELLOWORLD
