from aiogram import types, Dispatcher

from main_bot.filters.private_chat import IsPrivate
from main_bot.misc.parse_news import ParseBleacherReport


async def news(message: types.Message) -> None:
    parse = ParseBleacherReport().parse_posts()
    if not parse:
        await message.answer("Новостей пока нет)")
        return
    for i in parse:
        text = [
            f"{i['post_title']}: {i['link']}\n",
            f"Источник: {i['proof']}"
        ]
        await message.answer("\n".join(text))


def register_news_handlers(dispatcher: Dispatcher):
    dispatcher.register_message_handler(news, IsPrivate(), commands=["news"], commands_prefix="!/", state="*")
