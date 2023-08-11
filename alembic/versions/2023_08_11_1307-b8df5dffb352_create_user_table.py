"""create user table

Revision ID: b8df5dffb352
Revises:
Create Date: 2023-08-11 13:07:14.941078

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b8df5dffb352'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('firstname', sa.String(255), nullable=False),
        sa.Column('lastname', sa.String(255), nullable=False),
        sa.Column('username', sa.String(255), nullable=False),
        sa.Column('password', sa.String(255), nullable=False)
    )


def downgrade() -> None:
    op.drop_table('users')
