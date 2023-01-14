"""empty message

Revision ID: 9a8603d8ef99
Revises: bef82fe84b49
Create Date: 2023-01-14 15:19:23.137561

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9a8603d8ef99'
down_revision = 'bef82fe84b49'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('conta', sa.Column('usuario_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'conta', 'usuario', ['usuario_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'conta', type_='foreignkey')
    op.drop_column('conta', 'usuario_id')
    # ### end Alembic commands ###