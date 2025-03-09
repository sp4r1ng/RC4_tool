import argparse
from rc4 import RC4

def main():
    parser = argparse.ArgumentParser(description="RC4 Encryption/Decryption Tool")
    parser.add_argument("key", help="The encryption key")
    parser.add_argument("input", help="The input file to encrypt/decrypt")
    parser.add_argument("output", help="The output file to save the result")
    
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--encrypt", action="store_true", help="Encrypt the input file")
    group.add_argument("--decrypt", action="store_true", help="Decrypt the input file")
    
    args = parser.parse_args()
    
    key = args.key.encode()
    rc4 = RC4(key)
    
    try:
        with open(args.input, "rb") as input_file:
            input_data = input_file.read()
    except FileNotFoundError:
        print(f"Error: The file '{args.input}' was not found.")
        return
    
    if args.encrypt:
        result = rc4.encrypt(input_data)
        print("Encryption completed successfully.")
    elif args.decrypt:
        result = rc4.decrypt(input_data)
        print("Decryption completed successfully.")
    
    try:
        with open(args.output, "wb") as output_file:
            output_file.write(result)
        print(f"Operation completed. Output saved to {args.output}")
    except IOError:
        print(f"Error: Unable to write to '{args.output}'")

if __name__ == "__main__":
    main()
