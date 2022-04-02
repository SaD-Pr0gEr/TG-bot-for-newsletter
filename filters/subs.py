from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message

from loader import DB


class IsSubscribed(BoundFilter):
    async def check(self, message: Message) -> bool:
        return DB.retrieve_user(message.from_user.id).is_subscribed is True


class IsNotSubscribed(BoundFilter):
    async def check(self, message: Message) -> bool:
        return DB.retrieve_user(message.from_user.id).is_subscribed is False
