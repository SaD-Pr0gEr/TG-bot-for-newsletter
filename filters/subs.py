from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message

from loader import DB


class IsSubscribed(BoundFilter):
    async def check(self, message: Message) -> bool:
        return bool(DB.get_user_from_subs(message.from_user.id))


class IsNotSubscribed(BoundFilter):
    async def check(self, message: Message) -> bool:
        return bool(DB.get_user_from_subs(message.from_user.id)) is False
