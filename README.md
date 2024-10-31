#Vigenère Cipher Encoder/Decoder

Description: 
    This project is an implementation of the Vigenère Cipher, a classic method of encryption that uses a keyword to encode and decode messages. It extends the Caesar Cipher by using a series of interwoven Caesar ciphers based on the letters of a keyword, making it more secure against frequency analysis.

Features:
    Encryption: Encode plaintext using a specified keyword.
    Decryption: Decode encrypted text using the original keyword.
    Flexible Keyword: Allows customizable keywords of any length.
    Simple Interface: Command-line interface (CLI) or web-based frontend for ease of use.
    Character Filtering: Supports alphabetic-only and case-insensitive encoding, ignoring spaces and special characters if desired.

How It Works:
    The Vigenère Cipher uses the positions of letters in the alphabet to shift each character based on a repeating keyword. Each letter in the keyword shifts the corresponding character in the plaintext. This method provides a polyalphabetic cipher, which is more resilient against standard cryptographic attacks than the Caesar Cipher.

For example:

    Plaintext: "HELLO WORLD"
    Keyword: "KEY"
    Encrypted Text: "RIJVS UYVJN"

Technologies Used:
    Python/JavaScript: Core logic for the cipher

Getting Started:
    Clone the repository and install any required dependencies. To encrypt run the encryption.py and to decrpyt run the decryption.py

    ```python
    git clone https://github.com/Jurioton/Vigen-re-cipher.git
    cd vigenere-cipher
    # for encrypting 
    python encryption.py
    # for decrytion
    python decryption.py

Future Improvements:
    With some UI features