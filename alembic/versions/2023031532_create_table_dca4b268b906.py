"""create  table

Revision ID: dca4b268b906
Revises: a3d16d2075dc
Create Date: 2023-03-15 23:32:46.421910

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "dca4b268b906"
down_revision = "a3d16d2075dc"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "band_pictures",
        sa.Column("id", sa.UUID(as_uuid=False), nullable=False),
        sa.Column("path", sa.String(length=60), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "association_band_pictures",
        sa.Column("band_id", sa.UUID(as_uuid=False), nullable=False),
        sa.Column("picture_id", sa.UUID(as_uuid=False), nullable=False),
        sa.ForeignKeyConstraint(
            ["band_id"],
            ["bands.id"],
        ),
        sa.ForeignKeyConstraint(
            ["picture_id"],
            ["band_pictures.id"],
        ),
        sa.PrimaryKeyConstraint("band_id", "picture_id"),
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
    op.drop_table("association_band_pictures")
    op.drop_table("band_pictures")
    # ### end Alembic commands ###