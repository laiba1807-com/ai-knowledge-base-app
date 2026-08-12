from sqlalchemy import text

from app.db.database import SessionLocal
from app.repositories.chunk_repository import ChunkRepository


with SessionLocal() as db:
    result = db.execute(text("SELECT 1"))
    print("Database session OK:", result.scalar())

    repository = ChunkRepository(db)
    print("ChunkRepository OK:", repository)
