"""empty message

Revision ID: 3f446d057054
Revises: 2aa2d7a6838c
Create Date: 2015-12-20 14:14:53.597052

"""

# revision identifiers, used by Alembic.
revision = '3f446d057054'
down_revision = '2aa2d7a6838c'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('programme', sa.Column('period', sa.String(length=80), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('programme', 'period')
    ### end Alembic commands ###