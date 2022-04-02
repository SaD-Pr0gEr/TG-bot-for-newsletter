from aiogram import types
from aiogram.dispatcher.filters import Command

from filters.private_chat import IsPrivate
from loader import dp
from parsers.parse_news import ParseBleacherReport


@dp.message_handler(Command("news", prefixes="!/"), IsPrivate())
async def news(message: types.Message):
    parse = ParseBleacherReport().parse_posts()
    for i in parse:
        text = [
            f"{i['post_title']}: {i['link']}\n",
            f"Источник: {i['proof']}"
        ]
        await message.answer("\n".join(text))
