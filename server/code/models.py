# coding: utf-8
from sqlalchemy import ARRAY, Column, Date, Integer, Text, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, server_default=text("nextval('posts_id_seq'::regclass)"))
    rubrics = Column(ARRAY(Text()), nullable=False)
    text = Column(Text, nullable=False)
    created_date = Column(Date, nullable=False)