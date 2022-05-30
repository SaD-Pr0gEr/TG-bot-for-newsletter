from aiogram import types
from aiogram.dispatcher.filters import Command

from filters.private_chat import IsPrivate
from loader import dp, DB


@dp.message_handler(Command("start", prefixes="!/"), IsPrivate())
async def start(message: types.Message) -> None:
    if not DB.retrieve_user(message.from_user.id):
        DB.add_user(user_id=message.from_user.id, status=False)
    await message.answer(f'Привет, {message.from_user.first_name}! '
                         f'ты успешно запустил новостной бот команды Boston Celtics!')
