from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

key = DES3.adjust_key_parity(get_random_bytes(24))
iv = get_random_bytes(8)
cipher = DES3.new(key, DES3.MODE_CBC, iv)

plaintext = b'This is a secret message that spans multiple blocks.'
ciphertext = cipher.encrypt(pad(plaintext, DES3.block_size))

corrupted = bytearray(ciphertext)
corrupted[8] ^= 0xFF  # flip bits in second block

decipher = DES3.new(key, DES3.MODE_CBC, iv)
try:
    decrypted = unpad(decipher.decrypt(bytes(corrupted)), DES3.block_size)
except:
    decrypted = b'[Decryption failed due to padding error]'

print("Original Plaintext :", plaintext)
print("Corrupted Ciphertext:", corrupted.hex())
print("Decrypted Output    :", decrypted)
#output
Original Plaintext : b'This is a secret message that spans multiple blocks.'
Corrupted Ciphertext: 3f2c1a...<hex with flipped byte>...
Decrypted Output    : b'This is a \x9c\x8f\x1f...<garbled>...multiple blocks.'



