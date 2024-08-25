import os
import dotenv
dotenv.load_dotenv('/opt/airflow/secrets/.env')

class AppConfig(object):
    """
    Access environment variables here.
    """
    def __init__(self):
        """
        Load secret to config
        """
    ENV = os.getenv("ENV","dev")
    REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT = os.getenv("REDIS_PORT", 6379)

    TIME_ZONE = "Asia/Ho_Chi_Minh"

config = AppConfig()