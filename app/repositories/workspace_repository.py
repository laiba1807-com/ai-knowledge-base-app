from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.workspace import Workspace


class WorkspaceRepository:

    def __init__(self, session: Session):
        self.session = session

    def create(
        self,
        user_id: int,
        name: str,
    ) -> Workspace:
        workspace = Workspace(
            user_id=user_id,
            name=name,
        )

        self.session.add(workspace)
        self.session.flush()

        return workspace

    def get_by_id(
        self,
        workspace_id: int,
    ) -> Workspace | None:
        statement = select(Workspace).where(
            Workspace.id == workspace_id
        )

        return self.session.scalar(statement)

    def list_by_user(
        self,
        user_id: int,
    ) -> list[Workspace]:
        statement = (
            select(Workspace)
            .where(Workspace.user_id == user_id)
            .order_by(Workspace.created_at.desc())
        )

        return list(self.session.scalars(statement).all())

