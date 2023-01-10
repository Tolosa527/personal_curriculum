import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="config.env")

config_variables = {
    "gmail_api_key": os.getenv('GMAIL_API_KEY'),
    "gmail_name": os.getenv('GMAIL_NAME')
}

def get_config_variable(variable_name: str) -> str:
    return config_variables.get(variable_name)