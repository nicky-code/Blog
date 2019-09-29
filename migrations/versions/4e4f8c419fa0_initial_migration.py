"""Initial Migration

Revision ID: 4e4f8c419fa0
Revises: a097a682e0f9
Create Date: 2019-09-29 23:11:56.418732

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4e4f8c419fa0'
down_revision = 'a097a682e0f9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogs', sa.Column('feedback', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('blogs', 'feedback')
    # ### end Alembic commands ###