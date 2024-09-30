def generateKey(string, key):
    # Repeat the key to match the length of the string
    return (key * (len(string) // len(key) + 1))[:len(string)]

def encryption(string, key):
    return ''.join(chr((ord(s) + ord(k) - 2 * ord('A')) % 26 + ord('A')) for s, k in zip(string, key))

def decryption(encrypt_text, key):
    return ''.join(chr((ord(e) - ord(k) + 26) % 26 + ord('A')) for e, k in zip(encrypt_text, key))

if __name__ == "__main__":
    string = input("Enter the message: ").upper()
    keyword = input("Enter the keyword: ").upper()
    key = generateKey(string, keyword)
    encrypt_text = encryption(string, key)
    print("Encrypted message:", encrypt_text)
    print("Decrypted message:", decryption(encrypt_text, key))
