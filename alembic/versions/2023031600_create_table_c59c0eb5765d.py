"""create  table

Revision ID: c59c0eb5765d
Revises: 69f72b053cc7
Create Date: 2023-03-16 00:00:06.535122

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "c59c0eb5765d"
down_revision = "69f72b053cc7"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("association_band_pictures", "id")
    op.drop_column("associations_album_picture", "id")
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
    op.add_column(
        "associations_album_picture",
        sa.Column("id", sa.UUID(), autoincrement=False, nullable=False),
    )
    op.add_column(
        "association_band_pictures",
        sa.Column("id", sa.UUID(), autoincrement=False, nullable=False),
    )
    # ### end Alembic commands ###
