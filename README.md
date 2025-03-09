# RC4 Encryption/Decryption Tool

## Description
This tool is designed to perform encryption and decryption using the RC4 algorithm. The tool can encrypt or decrypt files using a provided key.

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/sp4r1ng/rc4_tool.git
    cd rc4_tool
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
### Encryption
Encrypt a file using the RC4 algorithm.

```sh
python main.py your_key input_file output_file --encrypt
```

### Decryption
Decrypt a file using the RC4 algorithm.

```sh
python main.py your_key input_file output_file --decrypt
```

## Example
To encrypt a file named `plaintext.txt` with the key `mysecretkey` and save the result to `ciphertext.txt`:

```sh
python main.py mysecretkey plaintext.txt ciphertext.txt --encrypt
```

To decrypt the file `ciphertext.txt` with the same key and save the result to `decrypted.txt`:

```sh
python main.py mysecretkey ciphertext.txt decrypted.txt --decrypt
```
