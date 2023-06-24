import psycopg2
from config import config

conn = psycopg2.connect(
    host=config.DB_HOST,
    database=config.DB_NAME,
    user=config.DB_USER,
    password=config.DB_PASS,
    port=config.DB_PORT,
    sslmode='require',
)
