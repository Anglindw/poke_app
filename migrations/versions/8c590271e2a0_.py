"""empty message

Revision ID: 8c590271e2a0
Revises: 
Create Date: 2022-12-05 23:54:26.564807

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8c590271e2a0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('pokedex',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('img_url', sa.String(), nullable=False),
    sa.Column('type', sa.String(length=50), nullable=False),
    sa.Column('ability', sa.String(length=50), nullable=False),
    sa.Column('hp', sa.String(length=50), nullable=False),
    sa.Column('attack', sa.String(length=50), nullable=False),
    sa.Column('defense', sa.String(length=50), nullable=False),
    sa.Column('special_attack', sa.String(length=50), nullable=False),
    sa.Column('special_defense', sa.String(length=50), nullable=False),
    sa.Column('speed', sa.String(length=50), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('img_url'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pokedex')
    op.drop_table('user')
    # ### end Alembic commands ###
