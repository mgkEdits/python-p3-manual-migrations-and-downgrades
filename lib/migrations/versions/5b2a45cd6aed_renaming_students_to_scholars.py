"""Renaming students to scholars

Revision ID: 5b2a45cd6aed
Revises: 791279dd0760
Create Date: 2023-12-19 07:44:52.788459

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5b2a45cd6aed'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')
    pass


def downgrade() -> None:
    op.rename_table('scholars', 'students')
    pass
