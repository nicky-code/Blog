"""snd Migration

Revision ID: 0ef0a4255906
Revises: 
Create Date: 2019-09-30 11:44:27.376352

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0ef0a4255906'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('writers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=100), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('pass_secure', sa.String(length=255), nullable=True),
    sa.Column('bio', sa.String(length=255), nullable=True),
    sa.Column('profile_pic_path', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_writers_email'), 'writers', ['email'], unique=True)
    op.create_foreign_key(None, 'blogs', 'writers', ['writer_id'], ['id'])
    op.create_foreign_key(None, 'comments', 'writers', ['writer_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_constraint(None, 'blogs', type_='foreignkey')
    op.drop_index(op.f('ix_writers_email'), table_name='writers')
    op.drop_table('writers')
    # ### end Alembic commands ###
