import os
from dotenv import load_dotenv

load_dotenv()


class Settings:

    AIRFLOW_BASE_URL = os.getenv(
        "AIRFLOW_BASE_URL",
        "http://localhost:8080/api/v1"
    )

    AIRFLOW_USERNAME = os.getenv(
        "AIRFLOW_USERNAME",
        "admin"
    )

    AIRFLOW_PASSWORD = os.getenv(
        "AIRFLOW_PASSWORD",
        "admin"
    )


settings = Settings()