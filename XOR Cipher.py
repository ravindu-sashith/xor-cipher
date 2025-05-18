def encrypt(plaintext, key):
    return ''.join(str(int(plaintext[i]) ^ int(key[i])) for i in range(len(plaintext)))

def decrypt(ciphertext, key):
    return ''.join(str(int(ciphertext[i]) ^ int(key[i])) for i in range(len(ciphertext)))

def main():
    
    plaintext = input("Enter a 4-bit plaintext: ")
    if len(plaintext) != 4 or not all(bit in '01' for bit in plaintext):
        print("Invalid plaintext. Please enter a 4-bit binary number.")
        return
    
    key = input("Enter a 4-bit key: ")
    if len(key) != 4 or not all(bit in '01' for bit in key):
        print("Invalid key. Please enter a 4-bit binary number.")
        return
    
    ciphertext = encrypt(plaintext, key)
    print("Ciphertext: " + ciphertext)
    
    decrypted_text = decrypt(ciphertext, key)
    print("Decrypted Text: " + decrypted_text)

    input('Press Return to exit')

if __name__ == "__main__":
    main()

