# daas_py_config  
## Project

Refrence of DaaS Project - https://github.com/nealrout/daas_docs

## Description
Project used to serve up configurations and secrets to other projects.  It is a wrapper on top of dynaconf.  

## Table of Contents
- [Requirements](#requirements)
- [Usage](#usage)
- [Features](#features)
- [Miscellaneous](#miscellaneous)
- [Contact](#contact)

## Requirements
__Set environment variables of parent project__  

ENV_FOR_DYNACONF=\<environment\>  
_i.e. development, integration, production_  

DYNACONF_SECRET_KEY=\<secret_key\>

This can be done in the environment itself, or using .env file using  
_from dotenv import load_dotenv_

## Usage
__Importing:__  
from daas_py_config import config

__Generate a new secret key:__  
python .\encrypt_helper.py --secret=True

__Encrypt .secrets.toml:__  
python .\encrypt_helper.py --encrypt=True  
_Script will ask for the secret_key required to decrypt_

__Decrypt .secrets.toml:__  
python .\encrypt_helper.py --decrypt=True  
_Script will ask for the secret_key required to decrypt_

#

## Features
- Configurations
  - config.get_configs()
  - config.get_secret(configuration_key, secret_key=None)
- Encrypted secrets
  - encrypt_helper.generate_secret_key()
  - encrypt_helper.encrypt_values()
  - encrypt_helper.decrypt_values()

## Miscellaneous

## Contact
Neal Routson  
nroutson@gmail.com