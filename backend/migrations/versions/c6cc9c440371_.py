"""empty message

Revision ID: c6cc9c440371
Revises: aa66e2ac397c
Create Date: 2022-05-22 15:13:56.168302

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c6cc9c440371'
down_revision = 'aa66e2ac397c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    t_contracts = op.create_table('contracts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('number', sa.String(length=50), nullable=False),
    sa.Column('start_date', sa.DateTime(timezone=True), nullable=False),
    sa.Column('end_date', sa.DateTime(timezone=True), nullable=False),
    sa.Column('supplier_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['supplier_id'], ['suppliers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###

    connection = op.get_bind()

    connection.execute(
        sa.insert(t_contracts).values([
            {
                'number': '12345678',
                'start_date': '2019-01-01',
                'end_date': '2026-01-01',
                'supplier_id': 1
            },
        ])
    )

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('contracts')
    # ### end Alembic commands ###
