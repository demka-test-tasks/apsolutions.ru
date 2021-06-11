# coding: utf-8
from sqlalchemy import BigInteger, Column, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Post(Base):
    __tablename__ = 'posts'

    id = Column(BigInteger, primary_key=True, index=True)
    text = Column(Text, nullable=False)
    created_date = Column(Text, nullable=False)
    rubrics = Column(Text, nullable=False)