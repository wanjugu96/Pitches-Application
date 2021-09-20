"""Initial Migration3

Revision ID: a511e5ed8edc
Revises: 467c0882e9d6
Create Date: 2021-09-20 18:26:59.608028

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a511e5ed8edc'
down_revision = '467c0882e9d6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('bio', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'bio')
    # ### end Alembic commands ###