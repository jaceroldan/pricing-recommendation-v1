import os
from dotenv import load_dotenv
from typing import Union, Literal


load_dotenv('.env')


class Config:
    def __init__(self) -> None:
        self.ENV: Union[Literal['production'], Literal['dev'],
                        Literal['development']] = os.getenv('ENV')
        self.PORT: str = os.getenv('PORT')
        self.DB_HOST: str = os.getenv('DB_HOST')
        self.DB_NAME: str = os.getenv('DB_NAME')
        self.DB_USER: str = os.getenv('DB_USER')
        self.DB_PASS: str = os.getenv('DB_PASS')
        self.DB_PORT: str = os.getenv('DB_PORT')
        self.DEBUG: bool = False if self.ENV == 'production' else True


config = Config()
