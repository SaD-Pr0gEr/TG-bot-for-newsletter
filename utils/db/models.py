from sqlalchemy import Column, Integer, Boolean, create_engine

from data.config import BASE, engine


class Subscribers(BASE):
    __tablename__ = "subscribers"

    ID = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    is_subscribed = Column(Boolean, default=False)

    def __init__(self, user_id: int, is_subscribed: bool = False) -> None:
        self.user_id = user_id
        self.is_subscribed = is_subscribed


if __name__ == "__main__":
    BASE.metadata.create_all(engine)
