"""add content column to posts table

Revision ID: 7f9d6be598f2
Revises: c6b79e5d1c7b
Create Date: 2025-11-29 16:49:44.419575

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7f9d6be598f2'
down_revision: Union[str, Sequence[str], None] = 'c6b79e5d1c7b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'content')
    pass
