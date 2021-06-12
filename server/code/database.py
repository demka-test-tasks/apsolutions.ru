import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SERVER_POSTGRES_CONNECTION = os.getenv("SERVER_POSTGRES_CONNECTION", None)

engine = create_engine(SERVER_POSTGRES_CONNECTION, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
