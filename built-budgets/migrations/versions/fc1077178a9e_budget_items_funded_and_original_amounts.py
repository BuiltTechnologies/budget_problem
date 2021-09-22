"""budget items funded and original amounts

Revision ID: fc1077178a9e
Revises: c7747a6d5092
Create Date: 2020-12-17 13:09:14.249828

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fc1077178a9e'
down_revision = 'c7747a6d5092'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('budget_items', sa.Column('funded_to_date', sa.String(length=20), nullable=False))
    op.add_column('budget_items', sa.Column('original_amount', sa.String(length=20), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('budget_items', 'original_amount')
    op.drop_column('budget_items', 'funded_to_date')
    # ### end Alembic commands ###
