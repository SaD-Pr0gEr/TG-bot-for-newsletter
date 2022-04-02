from aiogram import types
from aiogram.dispatcher.filters import Command

from filters.private_chat import IsPrivate
from filters.users import IsAdmin
from loader import dp, DB, bot


@dp.message_handler(Command("subscribers", prefixes="!/"), IsPrivate(), IsAdmin())
async def all_subscribers(message: types.Message):
    get = DB.get_all_subscribers()
    if not get:
        await message.answer("Подписчиков нет)")
        return
    for user in get:
        get_user = await bot.get_chat_member(user.user_id, message.from_user.id)
        await message.answer(f"@{get_user['user']['username'] or get_user['user']['id']}")


@dp.message_handler(Command("allusers", prefixes="!/"), IsPrivate(), IsAdmin())
async def all_users(message: types.Message):
    get = DB.get_all_users()
    if not get:
        await message.answer("Пользователей нет)")
        return
    for user in get:
        get_user = await bot.get_chat_member(user.user_id, message.from_user.id)
        await message.answer(f"@{get_user['user']['username'] or get_user['user']['id']}")


@dp.message_handler(Command("reset_data", prefixes="!/"), IsPrivate(), IsAdmin())
async def reset_data(message: types.Message):
    DB.reset_data()
    await message.answer("Данные успешно сброшены")
