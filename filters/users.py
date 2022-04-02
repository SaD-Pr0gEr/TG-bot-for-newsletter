from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message

from data.config import ADMIN_ID


class IsAdmin(BoundFilter):

    async def check(self, message: Message) -> bool:
        return int(message.from_user.id) == int(ADMIN_ID)
