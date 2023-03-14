"""create Track table

Revision ID: 0edf899cdf6d
Revises: b00ff4639599
Create Date: 2023-03-14 22:39:04.051119

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "0edf899cdf6d"
down_revision = "b00ff4639599"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "songs",
        sa.Column("id", sa.UUID(as_uuid=False), nullable=False),
        sa.Column("name", sa.String(length=60), nullable=False),
        sa.Column("num_song", sa.Integer(), nullable=False),
        sa.Column("album_id", sa.UUID(as_uuid=False), nullable=False),
        sa.ForeignKeyConstraint(
            ["album_id"],
            ["albums.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.add_column(
        "albums", sa.Column("commentary", sa.String(length=300), nullable=False)
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("albums", "commentary")
    op.drop_table("songs")
    # ### end Alembic commands ###