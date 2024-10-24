import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(".") / ".env"
# print(env_path)
load_dotenv(dotenv_path=env_path)

class Setting:
    PROJECT_TITLE: str = "Airbnb backend apis"
    PROJECT_VERSION: str = "0.1.0"
    # db stuff    
    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB")
    DATABASE_URL: str = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

    # SECRET_KEY: str = os.getenv("SECRET_KEY")
    # ALGORITHM: str = "HS256"
    # ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
settings = Setting()