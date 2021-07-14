from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Integer, Boolean, Column
import sys
sys.path.append("../")
from config import USER, PASSWORD, DB, HOST, PORT


engine = create_engine(f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}")

BASE = declarative_base()


class Subscribers(BASE):
    __tablename__ = "subscribers"

    ID = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    is_subscribed = Column(Boolean, default=False)


if __name__ == "__main__":
    BASE.metadata.create_all(engine)
