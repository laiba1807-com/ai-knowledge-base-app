from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.chat import Chat


class ChatRepository:

    def __init__(self, session: Session):
        self.session = session

    def create(
        self,
        workspace_id: int,
        title: str,
    ) -> Chat:
        chat = Chat(
            workspace_id=workspace_id,
            title=title,
        )

        self.session.add(chat)
        self.session.flush()

        return chat

    def get_by_id(
        self,
        chat_id: int,
    ) -> Chat | None:
        statement = select(Chat).where(
            Chat.id == chat_id
        )

        return self.session.scalar(statement)

    def list_by_workspace(
        self,
        workspace_id: int,
    ) -> list[Chat]:
        statement = (
            select(Chat)
            .where(Chat.workspace_id == workspace_id)
            .order_by(Chat.created_at.desc())
        )

        return list(self.session.scalars(statement).all())
