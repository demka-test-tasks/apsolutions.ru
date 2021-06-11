from database import Base
from sqlalchemy import BigInteger, Column, MetaData, Table, Text


class Post(Base):
    __tablename__ = "posts"

    id = Column('index', BigInteger, index=True),
    text = Column('text', Text),
    created_date = Column('created_date', Text),
    rubrics = Column('rubrics', Text)
