from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message

from loader import DB


class IsSubscribed(BoundFilter):
    async def check(self, message: Message) -> bool:
        user = DB.retrieve_user(message.from_user.id)
        return user.is_subscribed is True if user else None


class IsNotSubscribed(BoundFilter):
    async def check(self, message: Message) -> bool:
        user = DB.retrieve_user(message.from_user.id)
        return user.is_subscribed is False if user else None
