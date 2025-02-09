import os
from dynaconf import Dynaconf
from cryptography.fernet import Fernet
from daas_py_common.logging_config import logger

# Get the absolute path to the daas_py_config directory
current_dir = os.path.dirname(os.path.abspath(__file__))
settings_files = [os.path.join(current_dir, 'settings.toml')]

# Include .secrets.toml if necessary
secrets_file = os.path.join(current_dir, '.secrets.toml')
if os.path.exists(secrets_file):
     settings_files.append(secrets_file)

settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=settings_files,
    environments=True,  # Enable environment-based settings
    merge_enabled=True,
)

def get_configs():
    # for key, value in settings.items():
    #     logger.debug(f"{key}: {value}")
    # logger.debug (settings.as_dict())
    return settings

def get_secret(configuration_key, secret_key=None):
    if not configuration_key:
        raise ValueError("Configuration key is required to retrieve the secret.")
    
    if not secret_key:
        secret_key = os.environ.get('DYNACONF_SECRET_KEY')
    
    if not secret_key:
        raise ValueError("Secret key is required to decrypt the configuration.")
    
    if configuration_key not in get_configs():
        raise KeyError(f"Configuration key '{configuration_key}' does not exist in the settings.")

    cipher_suite = Fernet(secret_key)

    # Decrypt the secret data
    decrypted_config = cipher_suite.decrypt(get_configs()[configuration_key].encode())

    return decrypted_config.decode()

