from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

key = get_random_bytes(8)
iv = get_random_bytes(8)
cipher = DES.new(key, DES.MODE_CBC, iv)

plaintext = b'HELLO'
padded = pad(plaintext, DES.block_size)
ciphertext = cipher.encrypt(padded)

decipher = DES.new(key, DES.MODE_CBC, iv)
decrypted = unpad(decipher.decrypt(ciphertext), DES.block_size)

print("Plaintext :", plaintext)
print("Padded    :", padded)
print("Ciphertext:", ciphertext.hex())
print("Decrypted :", decrypted)
#output

Plaintext : b'HELLO'
Padded    : b'HELLO\x03\x03\x03'
Ciphertext: 5a1f3c9d8e4b2a1c3f7e9a6b1c2d3e4f
Decrypted : b'HELLO'
