import os
from cryptmoji import encrypt

source_file = input("Enter the file that needs to be encrypted: ")
key = input("Enter the key for encryption: ")

filename, extension = os.path.splitext(source_file)
destination_file = f"{filename}_encrypted{extension}"

with open(source_file, "r") as source:
    content = source.read()

repeated_keyword = (key * (len(content) // len(key) + 1))[:len(content)] 


with open(destination_file, "w") as encrypted:
    for i, j in zip(content, repeated_keyword):
        if i.isalpha():
            offset = ord('A') if i.isupper() else ord('a')
            letter = chr((ord(i) - offset + (ord(j.upper()) - ord('A'))) % 26 + offset)
        else:
            letter = i
        encrypted.write(letter)

print(f"Encryption completed successfully! Encrypted content saved to {destination_file}")
