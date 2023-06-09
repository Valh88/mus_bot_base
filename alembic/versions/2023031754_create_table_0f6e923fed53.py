"""create  table

Revision ID: 0f6e923fed53
Revises: 64941cdbfb4e
Create Date: 2023-03-17 19:54:34.947536

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "0f6e923fed53"
down_revision = "64941cdbfb4e"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "bands", "description", existing_type=sa.VARCHAR(length=800), nullable=True
    )
    op.alter_column(
        "bands", "themes", existing_type=sa.VARCHAR(length=100), nullable=True
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
        "bands", "themes", existing_type=sa.VARCHAR(length=100), nullable=False
    )
    op.alter_column(
        "bands", "description", existing_type=sa.VARCHAR(length=800), nullable=False
    )
    # ### end Alembic commands ###
