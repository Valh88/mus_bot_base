"""create  table

Revision ID: 7c16de3536b0
Revises: 584cf4a8f251
Create Date: 2023-03-18 23:51:56.314662

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "7c16de3536b0"
down_revision = "584cf4a8f251"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "albums",
        "release_date",
        existing_type=postgresql.TIMESTAMP(),
        type_=sa.Date(),
        existing_nullable=False,
    )
    op.alter_column(
        "songs",
        "sound_time",
        existing_type=sa.REAL(),
        type_=sa.Float(precision=3),
        existing_nullable=False,
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "songs",
        "sound_time",
        existing_type=sa.Float(precision=3),
        type_=sa.REAL(),
        existing_nullable=False,
    )
    op.alter_column(
        "albums",
        "release_date",
        existing_type=sa.Date(),
        type_=postgresql.TIMESTAMP(),
        existing_nullable=False,
    )
    # ### end Alembic commands ###