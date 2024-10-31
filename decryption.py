import os

encrypted_file = input("Enter the encrypted file to decrypt: ")
key = input("Enter the key for decryption: ")

filename, extension = os.path.splitext(encrypted_file)
destination_file = f"{filename}_decrypted{extension}"

if not os.path.isfile(encrypted_file):
    print("Encrypted file not found. Please check the path and try again.")
else:
    with open(encrypted_file, "r") as encrypted:
        content = encrypted.read()

    repeated_keyword = (key * (len(content) // len(key) + 1))[:len(content)] 

    with open(destination_file, "w") as decrypted:
        for i, j in zip(content, repeated_keyword):
            if i.isalpha(): 
                offset = ord('A') if i.isupper() else ord('a')
                letter = chr((ord(i) - offset - (ord(j.upper()) - ord('A'))) % 26 + offset)
            else:
                letter = i 
            decrypted.write(letter)

    print(f"Decryption completed successfully! Decrypted content saved to {destination_file}")
