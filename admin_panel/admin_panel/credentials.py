from utils import get_env_value

from dotenv import load_dotenv

load_dotenv()


POSTGRES_HOST = get_env_value("POSTGRES_HOST")
POSTGRES_PORT = get_env_value("POSTGRES_PORT")
POSTGRES_USERNAME = get_env_value("POSTGRES_USERNAME")
POSTGRES_PASSWORD = get_env_value("POSTGRES_PASSWORD")
POSTGRES_DB = get_env_value("POSTGRES_DB")

