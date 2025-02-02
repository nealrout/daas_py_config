# config

# To activate the virtual environment for this project
.\.venv\Scripts\activate

# To install all modules in requirements.txt
pip install -r requirements.txt

# To create new config project
dynaconf init -f toml

# To generate secrety key
see encrypt_helper.py
    generate_secret_key()

# To encrypt secrets
see encrypt_helper.py
    encrypt_values()