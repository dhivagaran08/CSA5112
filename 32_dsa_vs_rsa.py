from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dsa, rsa, padding
from cryptography.hazmat.primitives import serialization

def dsa_signature_demo(message):
    print("=== DSA Signature ===")
    private_key = dsa.generate_private_key(key_size=2048)
    public_key = private_key.public_key()

    signature = private_key.sign(message, hashes.SHA256())
    print(f"Signature: {signature.hex()}")

    try:
        public_key.verify(signature, message, hashes.SHA256())
        print("✅ DSA signature verified successfully.")
    except Exception as e:
        print("❌ DSA signature verification failed:", e)

def rsa_signature_demo(message):
    print("\n=== RSA Signature ===")
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()

    signature = private_key.sign(
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print(f"Signature: {signature.hex()}")

    try:
        public_key.verify(
            signature,
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        print("✅ RSA signature verified successfully.")
    except Exception as e:
        print("❌ RSA signature verification failed:", e)

if __name__ == "__main__":
    message = b"Secure message for signing"
    dsa_signature_demo(message)
    rsa_signature_demo(message)
#output
=== DSA Signature ===
Signature: <hexadecimal representation of the DSA signature>
✅ DSA signature verified successfully.

=== RSA Signature ===
Signature: <hexadecimal representation of the RSA signature>
✅ RSA signature verified successfully.

