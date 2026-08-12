"""add hnsw vector index

Revision ID: 3800c5fda166
Revises: 7647320adde6
Create Date: 2026-08-12 23:22:25.832238

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3800c5fda166'
down_revision: Union[str, Sequence[str], None] = '7647320adde6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute("""
        CREATE INDEX ix_chunks_embedding_hnsw
        ON chunks
        USING hnsw (embedding vector_cosine_ops)
    """)

def downgrade() -> None:
    """Downgrade schema."""
    op.execute("""
        DROP INDEX IF EXISTS ix_chunks_embedding_hnsw
    """)
