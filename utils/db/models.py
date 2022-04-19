from sqlalchemy import Column, Integer, Boolean

from data.config import BASE, engine


class Subscribers(BASE):
    __tablename__ = "subscribers"

    ID = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    is_subscribed = Column(Boolean, default=False)


if __name__ == "__main__":
    BASE.metadata.create_all(engine)
