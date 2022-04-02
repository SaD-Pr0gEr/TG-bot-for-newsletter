from aiogram import types
from aiogram.dispatcher.filters import Command

from filters.private_chat import IsPrivate
from loader import dp


@dp.message_handler(Command("start", prefixes="!/"), IsPrivate())
async def start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.first_name}! '
                         f'ты успешно запустил новостной бот команды Boston Celtics!')
