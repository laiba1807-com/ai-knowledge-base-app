from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.document import Document


class DocumentRepository:

    def __init__(self, session: Session):
        self.session = session

    def create(
        self,
        workspace_id: int,
        filename: str,
    ) -> Document:
        document = Document(
            workspace_id=workspace_id,
            filename=filename,
        )

        self.session.add(document)
        self.session.flush()

        return document

    def get_by_id(
        self,
        document_id: int,
    ) -> Document | None:
        statement = select(Document).where(
            Document.id == document_id
        )

        return self.session.scalar(statement)

    def list_by_workspace(
        self,
        workspace_id: int,
    ) -> list[Document]:
        statement = (
            select(Document)
            .where(Document.workspace_id == workspace_id)
            .order_by(Document.created_at.desc())
        )

        return list(self.session.scalars(statement).all())

    def update_status(
        self,
        document_id: int,
        status: str,
        error: str | None = None,
    ) -> Document | None:
        document = self.get_by_id(document_id)

        if document is None:
            return None

        document.status = status
        document.error = error

        self.session.flush()

        return document
