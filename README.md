# Vigenère Cipher Encoder/Decoder

A Python implementation of the **Vigenère Cipher**, a classic encryption method using a keyword to encode and decode messages. Unlike the Caesar Cipher, this method uses a series of interwoven Caesar ciphers based on the letters of a keyword, adding security against frequency analysis.

## Features
- **Encryption**: Encode plaintext using a specified keyword.
- **Decryption**: Decode encrypted text using the original keyword.
- **Flexible Keyword**: Supports customizable keywords of any length.
- **Character Filtering**: Ignores spaces and special characters if desired; alphabetic-only and case-insensitive.
- **Simple Interface**: Provides a command-line interface (CLI), with optional expansion for a web-based frontend.

## How It Works
The Vigenère Cipher shifts each character in the plaintext according to the corresponding character in a repeating keyword. This polyalphabetic approach strengthens the cipher against frequency-based attacks.

### Example
- **Plaintext**: `"HELLO WORLD"`
- **Keyword**: `"KEY"`
- **Encrypted Text**: `"RIJVS UYVJN"`

## Technologies Used
- **Python/JavaScript**: Core logic for encryption and decryption

## Getting Started
Clone the repository and install any required dependencies.

### Clone the repository:
```bash
git clone https://github.com/Jurioton/Vigen-re-cipher.git
cd vigenere-cipher
#for encrption
python encrytion.py
#for decryption
python decryption.py
```
## Future Improvements
-**User Interface**: Potential to expand into a web-based interface for ease of use

