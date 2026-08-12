from sqlalchemy.orm import Session

from app.models.chunk import Chunk


class ChunkRepository:

    def __init__(self, session: Session):
        self.session = session

    def create(
        self,
        document_id: int,
        page_number: int,
        text: str,
        token_count: int,
        embedding: list[float],
    ) -> Chunk:
        chunk = Chunk(
            document_id=document_id,
            page_number=page_number,
            text=text,
            token_count=token_count,
            embedding=embedding,
        )

        self.session.add(chunk)
        self.session.flush()

        return chunk
