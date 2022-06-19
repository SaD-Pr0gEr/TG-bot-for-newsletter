from aiogram import types, Dispatcher

from main_bot.filters.private_chat import IsPrivate
from main_bot.filters.subs import IsSubscribed, IsNotSubscribed
from main_bot.models.models import Users


async def subscribe(message: types.Message) -> None:
    await Users.set_status(message.from_user.id, status=True)
    await message.answer(
        "Вы успешно подписались на рассылку! Ждите от нас много спама))"
    )


async def unsubscribe(message: types.Message) -> None:
    await Users.set_status(message.from_user.id, False)
    await message.answer(
        f"Вы успешно отписались {message.from_user.first_name})"
    )


def register_subscribe_handlers(dispatcher: Dispatcher):
    dispatcher.register_message_handler(
        subscribe,
        IsPrivate(),
        IsNotSubscribed(),
        commands=["subscribe"],
        commands_prefix="!/",
        state="*"
    )
    dispatcher.register_message_handler(
        unsubscribe,
        IsPrivate(),
        IsSubscribed(),
        commands=["unsubscribe"],
        commands_prefix="!/",
        state="*"
    )
