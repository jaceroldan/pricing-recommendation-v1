import psycopg2
from config import DB_NAME, DB_PASS, DB_PORT, DB_USER, DB_HOST

conn = psycopg2.connect(
    host=DB_HOST,
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASS,
    port=DB_PORT,
    sslmode='require',
)
