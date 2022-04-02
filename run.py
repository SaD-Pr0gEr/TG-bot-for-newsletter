import asyncio

from aiogram import Dispatcher
from aiogram.utils import executor

from handlers import dp
from utils.init_commands import set_default_commands
from utils.mailing import send_news


async def on_startup(dispatcher: Dispatcher):
    await set_default_commands(dispatcher)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(send_news(16000))
    executor.start_polling(
        dp,
        on_startup=on_startup,
        skip_updates=True
    )
