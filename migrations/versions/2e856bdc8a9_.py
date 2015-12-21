"""empty message

Revision ID: 2e856bdc8a9
Revises: None
Create Date: 2015-12-19 17:22:05.158577

"""

# revision identifiers, used by Alembic.
revision = '2e856bdc8a9'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('programme', sa.Column('overview', sa.String(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('programme', 'overview')
    ### end Alembic commands ###