from pydantic import BaseSettings

class Settings(BaseSettings):
    
    sample_size: int=1000000
    partitions: int=8


settings = Settings()