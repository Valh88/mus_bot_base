"""create  table

Revision ID: 9deafc64256b
Revises: 05f5d5e4d77f
Create Date: 2023-03-18 13:55:48.374118

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "9deafc64256b"
down_revision = "05f5d5e4d77f"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "band_pictures",
        "path",
        existing_type=sa.VARCHAR(length=60),
        type_=sa.String(length=300),
        existing_nullable=True,
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
        "band_pictures",
        "path",
        existing_type=sa.String(length=300),
        type_=sa.VARCHAR(length=60),
        existing_nullable=True,
    )
    # ### end Alembic commands ###
