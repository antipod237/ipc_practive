"""empty message

Revision ID: 17e056ec2c58
Revises: 75a5e112cc70
Create Date: 2022-06-08 17:03:30.952365

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '17e056ec2c58'
down_revision = '75a5e112cc70'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    t_sales = op.create_table('sales',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('store_item_id', sa.Integer(), nullable=False),
    sa.Column('value', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.ForeignKeyConstraint(['store_item_id'], ['store_items.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_unique_constraint(None, 'store_items', ['name'])
    # ### end Alembic commands ###

    connection = op.get_bind()

    connection.execute(
        sa.insert(t_sales).values([
            {
                'store_item_id': 1,
                'value': 3,
                'date': '2021-01-04'
            },
        ])
    )


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sales')
    # ### end Alembic commands ###
