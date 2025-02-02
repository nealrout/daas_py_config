import os
from config import settings
from dynaconf import Dynaconf
from cryptography.fernet import Fernet
from daas_py_common.logging_config import logger

def get_configs():
    return settings

def get_secret(configuration_key, secret_key=None):
    if not configuration_key:
        raise ValueError("Configuration key is required to retrieve the secret.")
    if not secret_key:
        secret_key = os.environ.get('DYNACONF_SECRET_KEY')

    cipher_suite = Fernet(secret_key)

    # Decrypt the secret data
    decrypted_config = cipher_suite.decrypt(get_configs()[configuration_key].encode())

    return decrypted_config.decode()


# if __name__ == "__main__":
    # os.environ['ENV_FOR_DYNACONF'] = 'development'
    # os.environ['DYNACONF_SECRET_KEY'] = ''
    # secret_key = os.environ.get('DYNACONF_SECRET_KEY')
    
    # get_secret('DATABASE_PASSWORD')
    # configs = get_configs()
    # print (configs)
    # print(configs.DATABASE_URL)
    # print(configs.API_KEY)
    # print(configs.LOG_LEVEL)
    # print(configs.get("DATABASE_PASSWORD"))    
