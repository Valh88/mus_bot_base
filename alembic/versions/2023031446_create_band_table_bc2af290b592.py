"""create band table

Revision ID: bc2af290b592
Revises: c7d16bc2ebbd
Create Date: 2023-03-14 18:46:56.314586

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "bc2af290b592"
down_revision = "c7d16bc2ebbd"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("bands", sa.Column("name", sa.String(length=60), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("bands", "name")
    # ### end Alembic commands ###
