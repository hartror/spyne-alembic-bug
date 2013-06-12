"""
Test case for spyne/alembic bug
"""

from spyne.model.primitive import Unicode
from spyne.model.complex import Array
from spyne.model.complex import TTableModel

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

TableModel = TTableModel(Base.metadata)


class Example(TableModel):
    
    __tablename__ = 'examples'

    id = Unicode(pk=True, min_occurs=1, nillable=False)
    a_list = Array(Unicode, min_occurs=1, nillable=False).store_as('xml')
    new_column = Unicode(pk=True, min_occurs=1, nillable=False)
