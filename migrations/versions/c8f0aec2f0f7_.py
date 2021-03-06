"""empty message

Revision ID: c8f0aec2f0f7
Revises: None
Create Date: 2016-02-26 03:08:32.182555

"""

# revision identifiers, used by Alembic.
revision = 'c8f0aec2f0f7'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('myprofile', sa.Column('age', sa.Integer(), nullable=True))
    op.add_column('myprofile', sa.Column('image', sa.String(length=120), nullable=True))
    op.add_column('myprofile', sa.Column('option', sa.String(length=20), nullable=True))
    op.drop_constraint(u'myprofile_nickname_key', 'myprofile', type_='unique')
    op.drop_column('myprofile', 'nickname')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('myprofile', sa.Column('nickname', sa.VARCHAR(length=80), autoincrement=False, nullable=True))
    op.create_unique_constraint(u'myprofile_nickname_key', 'myprofile', ['nickname'])
    op.drop_column('myprofile', 'option')
    op.drop_column('myprofile', 'image')
    op.drop_column('myprofile', 'age')
    ### end Alembic commands ###
