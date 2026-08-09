import os

import psycopg
from dotenv import load_dotenv


load_dotenv()

database_url = os.getenv("DATABASE_URL")

if not database_url:
    raise RuntimeError("DATABASE_URL is not set")

if "+psycopg" in database_url:
    database_url = database_url.replace("+psycopg", "")


with psycopg.connect(database_url) as connection:
    with connection.cursor() as cursor:

        # Test PostgreSQL connection
        cursor.execute("SELECT version();")
        version = cursor.fetchone()

        print("Database connection successful!")
        print(version[0])

        # Enable pgvector
        cursor.execute("CREATE EXTENSION IF NOT EXISTS vector;")

        # Verify pgvector
        cursor.execute(
            "SELECT extname FROM pg_extension WHERE extname = 'vector';"
        )
        extension = cursor.fetchone()

        if extension:
            print("pgvector extension is enabled!")
        else:
            print("pgvector extension was NOT found!")