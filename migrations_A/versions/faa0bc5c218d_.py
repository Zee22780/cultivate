"""empty message

Revision ID: faa0bc5c218d
Revises: 3e87f4175613
Create Date: 2022-04-11 15:27:58.670475

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'faa0bc5c218d'
down_revision = '3e87f4175613'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('flashcards',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('collection', sa.String(length=140), nullable=False),
    sa.Column('front', sa.String(), nullable=True),
    sa.Column('back', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('collections')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('collections',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(length=140), autoincrement=False, nullable=False),
    sa.Column('flashcard', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='collections_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='collections_pkey')
    )
    op.drop_table('flashcards')
    # ### end Alembic commands ###