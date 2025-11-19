from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def padding_demo():
    key = get_random_bytes(8)  # DES requires 8-byte key
    cipher = DES.new(key, DES.MODE_ECB)

    message = b"Hello"  # Only 5 bytes, needs padding
    print("📨 Original:", message)

    # Padding the message to match DES block size
    padded = pad(message, DES.block_size)
    print("🧱 Padded:", padded)

    # Encrypt
    encrypted = cipher.encrypt(padded)
    print("🔒 Encrypted:", encrypted.hex())

    # Decrypt
    decrypted_padded = cipher.decrypt(encrypted)
    decrypted = unpad(decrypted_padded, DES.block_size)
    print("🔓 Decrypted:", decrypted)

if __name__ == "__main__":
    padding_demo()
#output

📨 Original: b'Hello'
🧱 Padded: b'Hello\x03\x03\x03'
🔒 Encrypted: 8f3c1e9a8b7d6c4f...
🔓 Decrypted: b'Hello'
