from gino import Gino
from sqlalchemy import Column, Integer, Boolean

from main_bot.models.mixins import BaseModelMixin

db = Gino()


class Users(db.Model, BaseModelMixin):
    __tablename__ = "subscribers"

    ID = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    is_subscribed = Column(Boolean, default=False)

    @classmethod
    async def retrieve(cls, user_id: int) -> object:
        return await cls.query.where(cls.user_id == user_id).gino.first()

    @classmethod
    async def all_subscribers(cls) -> list:
        return await cls.query.where(cls.is_subscribed == True).gino.all()

    @classmethod
    async def set_status(cls, user_id: int, status: bool) -> None:
        user = await cls.retrieve(user_id)
        await user.update(is_subscribed=status).apply()

    @classmethod
    async def add_user(cls, user_id: int):
        await cls.create(user_id=user_id, is_subscribed=False)

    def __str__(self):
        return f"{self.ID}: {self.user_id}"

    def __repr__(self):
        return f"Model {self.__tablename__}: {self.ID}"
