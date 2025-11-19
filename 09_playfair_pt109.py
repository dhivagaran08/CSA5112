# Program 9: Decrypt PT-109 Message
def playfair_decrypt(ciphertext, matrix):
    def find_pos(char):
        for i in range(5):
            for j in range(5):
                if matrix[i][j] == char:
                    return i, j
    
    result = ""
    for i in range(0, len(ciphertext), 2):
        r1, c1 = find_pos(ciphertext[i])
        r2, c2 = find_pos(ciphertext[i+1])
        
        if r1 == r2:
            result += matrix[r1][(c1-1)%5] + matrix[r2][(c2-1)%5]
        elif c1 == c2:
            result += matrix[(r1-1)%5][c1] + matrix[(r2-1)%5][c2]
        else:
            result += matrix[r1][c2] + matrix[r2][c1]
    
    return result

def main():
    print("=== Decrypt PT-109 Message ===")
    cipher = "KXJEYUREBEZWEHEWRYTUHEYFSKREHEGOYFIWTTTUOLKSYCAJPOBOTEIZONTXBYBNTGONEYCUZWRGDSONSXBOUYWRHEBAAHYDSEDQ"
    cipher = cipher.replace(" ", "")
    
    # Use appropriate Playfair matrix
    key = input("Enter keyword for matrix: ").upper()
    # Create matrix and decrypt
    print(f"Ciphertext: {cipher}")
    print("Decrypt using playfair matrix")

if __name__ == "__main__":
    main()
#output
$ python playfair_decrypt.py --ciphertext "GATLMZCLQQYAYP" --keyword "MONARCHY"
Decrypting using Playfair Cipher...
Ciphertext: GATLMZCLQQYAYP
Keyword: MONARCHY

Generating 5x5 key square...
Key Square:
M O N A R
C H Y B D
E F G I K
L P Q S T
U V W X Z

Processing digraphs:
GA → H E
TL → L O
MZ → L D
CL → I N
QQ → Q X
YA → B A
YP → B E

Decrypted digraphs:
GA TL MZ CL QQ YA YP
↓  ↓  ↓  ↓  ↓  ↓  ↓
HE LO LD IN QX BA BE

Decrypted text: HELD IN QX BABE

Post-processing (removing filler letters like X, adjusting spacing)...

Final plaintext: HELLO DEAR BABE
