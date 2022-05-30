from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message

from data.config import ADMINS


class IsAdmin(BoundFilter):

    async def check(self, message: Message) -> bool:
        return int(message.from_user.id) in list(map(int, ADMINS))
