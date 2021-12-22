from pydantic import BaseSettings

class Settings(BaseSettings):
    
    sample_size: int
    partitions: int=8


settings = Settings()