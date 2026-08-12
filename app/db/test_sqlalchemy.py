from sqlalchemy import text

from app.db.database import engine


with engine.connect() as connection:
    result = connection.execute(text("SELECT version();"))
    version = result.fetchone()

    print("SQLAlchemy connection successful!")
    print(version[0])
