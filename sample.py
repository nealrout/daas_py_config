import sys
import os

# Get the current working directory (CWD) of the script
cwd = os.getcwd()
# Build the relative path to the sibling project
# project_path = os.path.abspath(os.path.join(cwd, '..', 'daas_py_config'))
project_path = os.path.abspath(os.path.join(cwd, '..'))
# Add the project path to sys.path
sys.path.insert(0, project_path)

from daas_py_config import config
from daas_py_common.logging_config import logger

if __name__ == "__main__":
    logger.info("Starting the main function")
    # set these variables in .env file of parent project.
    # os.environ['ENV_FOR_DYNACONF'] = 'development'
    # os.environ['DYNACONF_SECRET_KEY'] = 'ASDF'
    configs = config.get_configs()
    
    asdf = config.get_secret('DATABASE_PASSWORD')

    logger.info("Finished the main function")