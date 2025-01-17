"""uniqe_passport_number

Revision ID: 7415503b7089
Revises: 9714e58fb9c2
Create Date: 2024-04-22 19:27:44.120413

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision: str = "7415503b7089"
down_revision: Union[str, None] = "9714e58fb9c2"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, "payments", ["passport_number"])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "payments", type_="unique")
    # ### end Alembic commands ###
