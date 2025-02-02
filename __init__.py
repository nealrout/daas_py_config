from main import get_secret, get_configs

# Package-level variable
PACKAGE_NAME = "daas_config"

# Package-level initialization
print(f"Initializing package {PACKAGE_NAME}")

# Package-level function
def initialize():
    print("Package initialized")

__all__ = ["initialize", "PACKAGE_NAME"]