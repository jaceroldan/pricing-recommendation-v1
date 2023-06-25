import psycopg2
from config import config

conn = psycopg2.connect(
    **config.db_config(),
    sslmode='require',
)
