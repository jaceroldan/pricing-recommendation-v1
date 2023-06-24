import os
from dotenv import load_dotenv
from typing import Union, Literal


load_dotenv('.env')


class Config:
    ENV: Union[Literal['production'], Literal['dev'], Literal['development']]
    PORT: str
    DB_HOST: str
    DB_NAME: str
    DB_USER: str
    DB_PASS: str
    DB_PORT: str
    DEBUG: bool = True

    def __init__(self) -> None:
        self.ENV = os.getenv('ENV')
        self.PORT = os.getenv('PORT')
        self.DB_HOST = os.getenv('DB_HOST')
        self.DB_NAME = os.getenv('DB_NAME')
        self.DB_USER = os.getenv('DB_USER')
        self.DB_PASS = os.getenv('DB_PASS')
        self.DB_PORT = os.getenv('DB_PORT')

        if self.ENV == 'production':
            self.DEBUG = False


config = Config()
