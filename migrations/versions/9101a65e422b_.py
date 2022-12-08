"""empty message

Revision ID: 9101a65e422b
Revises: f3f01296d2fa
Create Date: 2022-12-07 18:09:20.274036

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9101a65e422b'
down_revision = 'f3f01296d2fa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pokedex', schema=None) as batch_op:
        batch_op.drop_column('type')

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('username',
               existing_type=sa.VARCHAR(length=50),
               type_=sa.String(length=200),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('username',
               existing_type=sa.String(length=200),
               type_=sa.VARCHAR(length=50),
               existing_nullable=False)

    with op.batch_alter_table('pokedex', schema=None) as batch_op:
        batch_op.add_column(sa.Column('type', sa.VARCHAR(length=50), autoincrement=False, nullable=False))

    # ### end Alembic commands ###