from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.message import Message


class MessageRepository:

    def __init__(self, session: Session):
        self.session = session

    def create(
        self,
        chat_id: int,
        role: str,
        content: str,
    ) -> Message:
        message = Message(
            chat_id=chat_id,
            role=role,
            content=content,
        )

        self.session.add(message)
        self.session.flush()

        return message

    def get_by_id(
        self,
        message_id: int,
    ) -> Message | None:
        statement = select(Message).where(
            Message.id == message_id
        )

        return self.session.scalar(statement)

    def list_by_chat(
        self,
        chat_id: int,
    ) -> list[Message]:
        statement = (
            select(Message)
            .where(Message.chat_id == chat_id)
            .order_by(Message.created_at.asc())
        )

        return list(self.session.scalars(statement).all())
