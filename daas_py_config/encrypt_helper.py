import argparse
import toml
from cryptography.fernet import Fernet
import getpass
import os
import sys

# Get the current working directory (CWD) of the script
cwd = os.getcwd()
# Build the relative path to the sibling project
project_path = os.path.abspath(os.path.join(cwd, '..'))
# Add the project path to sys.path
sys.path.insert(0, project_path)

from daas_py_common.logging_config import logger

def generate_secret_key():
    # Generate a new secret key
    secret_key = Fernet.generate_key()
    return secret_key.decode()

def encrypt_values(file_path, secret_key):
    # Load the .secrets.toml file
    with open(file_path, 'r') as file:
        secrets = toml.load(file)

    cipher_suite = Fernet(secret_key)

    # Encrypt all values in the .secrets.toml file
    def encrypt_dict(data):
        encrypted_data = {}
        for key, value in data.items():
            if isinstance(value, dict):
                encrypted_data[key] = encrypt_dict(value)
            else:
                encrypted_data[key] = cipher_suite.encrypt(value.encode()).decode()
        return encrypted_data

    encrypted_secrets = encrypt_dict(secrets)

    # Save the encrypted values back to the .secrets.toml file
    with open(file_path, 'w') as file:
        toml.dump(encrypted_secrets, file)

    logger.info("All values in .secrets.toml have been encrypted.")

def decrypt_values(file_path, secret_key):
    # Load the encrypted .secrets.toml file
    with open(file_path, 'r') as file:
        encrypted_secrets = toml.load(file)

    cipher_suite = Fernet(secret_key)

    # Decrypt all values in the .secrets.toml file
    def decrypt_dict(data):
        decrypted_data = {}
        for key, value in data.items():
            if isinstance(value, dict):
                decrypted_data[key] = decrypt_dict(value)
            else:
                decrypted_data[key] = cipher_suite.decrypt(value.encode()).decode()
        return decrypted_data

    decrypted_secrets = decrypt_dict(encrypted_secrets)

    # Save the decrypted values back to the .secrets.toml file
    with open(file_path, 'w') as file:
        toml.dump(decrypted_secrets, file)

    logger.info("All values in .secrets.toml have been decrypted.")


def main():
    parser = argparse.ArgumentParser(description="Encrypt all values in .secrets.toml")
    parser.add_argument("--file_path", help="Path to the .secrets.toml file", required=False, type=str, default=".secrets.toml")
    parser.add_argument("--encrypt", help="Encrypt the secrets", required=False, default=False, type=bool)
    parser.add_argument("--decrypt", help="Descript the secrets", required=False, default=False, type=bool)
    parser.add_argument("--secret", help="Genearate new secret key", required=False, default=False, type=bool)

    args = parser.parse_args()

    secret_key = getpass.getpass(prompt="Enter the secret key: ")

    if secret_key:
        if args.decrypt:
            decrypt_values(args.file_path, secret_key.encode())
        if args.encrypt:
            encrypt_values(args.file_path, secret_key.encode())
    if args.secret:
        secret_key = generate_secret_key()
        logger.info(f"Generated secret key: {secret_key}")

if __name__ == "__main__":
    main()