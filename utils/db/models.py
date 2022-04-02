from sqlalchemy import create_engine, Column, Integer, Boolean
from sqlalchemy.ext.declarative import declarative_base

from data.config import DATABASE_URL


engine = create_engine(DATABASE_URL)
BASE = declarative_base()


class Subscribers(BASE):
    __tablename__ = "subscribers"

    ID = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    is_subscribed = Column(Boolean, default=False)


if __name__ == "__main__":
    BASE.metadata.create_all(engine)
