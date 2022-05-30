from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message

from main_bot.config import Config


class IsAdmin(BoundFilter):

    async def check(self, message: Message) -> bool:
        config: Config = message.bot.get("config")
        return int(message.from_user.id) in config.tg_bot.admin_ids
