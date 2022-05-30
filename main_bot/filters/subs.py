from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message

from main_bot.models.models import Users


class IsSubscribed(BoundFilter):

    async def check(self, message: Message) -> bool:
        user = await Users.retrieve(message.from_user.id)
        return user.is_subscribed


class IsNotSubscribed(BoundFilter):

    async def check(self, message: Message) -> bool:
        user = await Users.retrieve(message.from_user.id)
        return not user.is_subscribed
