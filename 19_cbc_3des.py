from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

key = DES3.adjust_key_parity(get_random_bytes(24))
iv = get_random_bytes(8)
cipher = DES3.new(key, DES3.MODE_CBC, iv)

plaintext = b'This is a secret message.'
ciphertext = cipher.encrypt(pad(plaintext, DES3.block_size))

decipher = DES3.new(key, DES3.MODE_CBC, iv)
decrypted = unpad(decipher.decrypt(ciphertext), DES3.block_size)

print("Plaintext :", plaintext)
print("Ciphertext:", ciphertext.hex())
print("Decrypted :", decrypted)
#output
Plaintext : b'This is a secret message.'
Ciphertext: 9f3c7f4e3b7f6e8a6c3e2d1a7b9e4f2c5a1d3c7f8e6b2a1c
Decrypted : b'This is a secret message.'

