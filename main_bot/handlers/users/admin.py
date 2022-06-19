from aiogram import types, Dispatcher

from main_bot.filters.private_chat import IsPrivate
from main_bot.filters.users import IsAdmin
from main_bot.models.models import Users


async def all_subscribers(message: types.Message) -> None:
    get = await Users.all_subscribers()
    if not get:
        await message.answer("Подписчиков нет)")
        return
    for user in get:
        await message.answer(
            f"User ID: {user.user_id}"
        )


async def all_users(message: types.Message) -> None:
    get = await Users.get_all()
    if not get:
        await message.answer("Пользователей нет)")
        return
    for user in get:
        await message.answer(
            f"User ID: {user.user_id}"
        )


async def reset_data(message: types.Message) -> None:
    await Users.reset_data()
    await message.answer("Данные успешно сброшены")


def register_admin_handlers(dispatcher: Dispatcher):
    dispatcher.register_message_handler(
        all_subscribers,
        IsPrivate(),
        IsAdmin(),
        commands=["subscribers"],
        commands_prefix="!/",
        state="*"
    )
    dispatcher.register_message_handler(
        all_users,
        IsPrivate(),
        IsAdmin(),
        commands=["allusers"],
        commands_prefix="!/",
        state="*"
    )
    dispatcher.register_message_handler(
        reset_data,
        IsPrivate(),
        IsAdmin(),
        commands=["reset_data"],
        commands_prefix="!/",
        state="*"
    )
