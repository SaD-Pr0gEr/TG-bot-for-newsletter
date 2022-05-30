from aiogram import types, Dispatcher

from main_bot.filters.private_chat import IsPrivate
from main_bot.models.models import Users


async def start(message: types.Message) -> None:
    if not await Users.retrieve(message.from_user.id):
        await Users.add_user(user_id=message.from_user.id)
    await message.answer(f'Привет, {message.from_user.first_name}! '
                         f'ты успешно запустил новостной бот команды Boston Celtics!')


def register_start_handlers(dispatcher: Dispatcher):
    dispatcher.register_message_handler(start, IsPrivate(), commands=["start"], commands_prefix="!/", state="*")
