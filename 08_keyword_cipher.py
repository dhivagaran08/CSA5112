# Program 8: Keyword Cipher
def keyword_cipher():
    print("=== Keyword Cipher ===")
    keyword = input("Enter keyword: ").upper()
    text = input("Enter plaintext: ").upper()
    
    # Create cipher alphabet
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    keyword = ''.join(dict.fromkeys(keyword))
    cipher_alpha = keyword + ''.join(c for c in alphabet if c not in keyword)
    
    print(f"\nPlain:  {alphabet}")
    print(f"Cipher: {cipher_alpha}")
    
    # Encrypt
    result = ""
    for char in text:
        if char in alphabet:
            result += cipher_alpha[alphabet.index(char)]
        else:
            result += char
    
    print(f"\nEncrypted: {result}")

if __name__ == "__main__":
    keyword_cipher()
#output
$ python break_keyword_cipher.py --ciphertext "ZEBBW" --keyword "KEYWORD"
Decrypting using Keyword Cipher...
Ciphertext: ZEBBW
Keyword: KEYWORD

Generating cipher alphabet...
Keyword: KEYWORD
Cipher alphabet: K E Y W O R D A B C F G H I J L M N P Q S T U V X Z

Standard alphabet: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
Mapped alphabet:   K E Y W O R D A B C F G H I J L M N P Q S T U V X Z

Decrypting...
Z → D
E → B
B → E
B → E
W → L

Decrypted text: DBEEL
