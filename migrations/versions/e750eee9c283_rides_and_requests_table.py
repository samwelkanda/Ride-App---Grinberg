"""rides and requests table

Revision ID: e750eee9c283
Revises: 95f4d5170787
Create Date: 2018-07-04 18:34:46.748243

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e750eee9c283'
down_revision = '95f4d5170787'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ride',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('start', sa.String(length=40), nullable=True),
    sa.Column('destination', sa.String(length=40), nullable=True),
    sa.Column('time', sa.String(length=40), nullable=True),
    sa.Column('seats', sa.Integer(), nullable=True),
    sa.Column('cost', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_ride_timestamp'), 'ride', ['timestamp'], unique=False)
    op.create_table('request',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pickup', sa.String(length=40), nullable=True),
    sa.Column('time', sa.String(length=40), nullable=True),
    sa.Column('seats', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('ride_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['ride_id'], ['ride.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_request_timestamp'), 'request', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_request_timestamp'), table_name='request')
    op.drop_table('request')
    op.drop_index(op.f('ix_ride_timestamp'), table_name='ride')
    op.drop_table('ride')
    # ### end Alembic commands ###