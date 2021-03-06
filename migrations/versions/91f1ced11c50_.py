"""empty message

Revision ID: 91f1ced11c50
Revises: 8821cc17655a
Create Date: 2019-03-30 15:34:52.260000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '91f1ced11c50'
down_revision = '8821cc17655a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column(u'user', sa.Column('role_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'user', 'role', ['role_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='foreignkey')
    op.drop_column(u'user', 'role_id')
    op.drop_table('role')
    # ### end Alembic commands ###
