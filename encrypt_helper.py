import argparse
import toml
from cryptography.fernet import Fernet
import getpass

def generate_secret_key():
    # Generate a new secret key
    secret_key = Fernet.generate_key()
    print(secret_key.decode())

def encrypt_secrets(secret_key):
    # Replace with your generated secret key
    cipher_suite = Fernet(secret_key)

    # Encrypt your secret data
    secret_data = b'supersecretpassword'
    encrypted_data = cipher_suite.encrypt(secret_data)

    print(encrypted_data.decode())


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

    print("All values in .secrets.toml have been encrypted.")


def main():
    parser = argparse.ArgumentParser(description="Encrypt all values in .secrets.toml")
    parser.add_argument("--file_path", help="Path to the .secrets.toml file", required=False, type=str, default=".secrets.toml")
    args = parser.parse_args()

    secret_key = getpass.getpass(prompt="Enter the secret key: ")

    if secret_key:
        encrypt_values(args.file_path, secret_key.encode())
    else:
        print("No secret key provided. Exiting.")

if __name__ == "__main__":
    main()