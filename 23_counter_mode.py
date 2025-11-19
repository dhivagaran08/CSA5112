from Crypto.Cipher import AES
from Crypto.Util import Counter
from Crypto.Random import get_random_bytes

key = get_random_bytes(16)
nonce = get_random_bytes(8)
ctr = Counter.new(64, prefix=nonce)
cipher = AES.new(key, AES.MODE_CTR, counter=ctr)

plaintext = b'Counter mode encrypts each block independently.'
ciphertext = cipher.encrypt(plaintext)

ctr_dec = Counter.new(64, prefix=nonce)
decipher = AES.new(key, AES.MODE_CTR, counter=ctr_dec)
decrypted = decipher.decrypt(ciphertext)

print("Plaintext :", plaintext)
print("Ciphertext:", ciphertext.hex())
print("Decrypted :", decrypted)
#output
Plaintext : b'Counter mode encrypts each block independently.'
Ciphertext: 8f3c7e2a9b1e4f6c3d2a1c7b9e6f2d1a...
Decrypted : b'Counter mode encrypts each block independently.'

