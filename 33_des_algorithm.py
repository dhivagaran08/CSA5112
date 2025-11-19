from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def des_demo():
    # DES requires 8-byte key and block size
    key = get_random_bytes(8)
    cipher = DES.new(key, DES.MODE_ECB)

    message = b"SecretMsg"  # Must be padded to 8-byte blocks
    padded_msg = pad(message, DES.block_size)

    # Encrypt
    ciphertext = cipher.encrypt(padded_msg)
    print("🔒 Encrypted:", ciphertext.hex())

    # Decrypt
    decipher = DES.new(key, DES.MODE_ECB)
    decrypted_padded = decipher.decrypt(ciphertext)
    decrypted = unpad(decrypted_padded, DES.block_size)
    print("🔓 Decrypted:", decrypted.decode())

if __name__ == "__main__":
    des_demo()
#output

🔒 Encrypted: 3f2c1e9a8b7d6c4f...
🔓 Decrypted: SecretMsg
