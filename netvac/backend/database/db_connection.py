import psycopg2
from decouple import config

def connect_to_db():
    """Connects to the PostgreSQL database and returns a connection object."""
    try:
        conn = psycopg2.connect(
            host=config('DB_HOST'),
            database=config('DB_NAME'),
            user=config('DB_USER'),
            password=config('DB_PASSWORD'),
            port=config('DB_PORT', cast=int)  # Cast port to integer
        )
        return conn
    except psycopg2.Error as e:
        print(f"Error connecting to database: {e}")
        return None

def close_connection(conn):
    """Closes the database connection."""
    if conn:
        conn.close()