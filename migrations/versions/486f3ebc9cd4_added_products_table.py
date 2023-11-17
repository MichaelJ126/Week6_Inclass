"""added products table

Revision ID: 486f3ebc9cd4
Revises: cabd222a09a3
Create Date: 2023-11-15 13:31:15.225967

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '486f3ebc9cd4'
down_revision = 'cabd222a09a3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('prod_id', sa.String(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('image', sa.String(), nullable=True),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.Column('prince', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('date_added', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('prod_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product')
    # ### end Alembic commands ###