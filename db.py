import psycopg2
from config import appConfig

conn = psycopg2.connect(
    host=appConfig.DB_HOST,
    database=appConfig.DB_NAME,
    user=appConfig.DB_USER,
    password=appConfig.DB_PASS,
    port=appConfig.DB_PORT,
    sslmode='require',
)
