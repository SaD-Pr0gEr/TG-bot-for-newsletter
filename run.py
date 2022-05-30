import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor

from main_bot.config import load_config
from main_bot.handlers.users.admin import register_admin_handlers
from main_bot.handlers.users.news import register_news_handlers
from main_bot.handlers.users.start import register_start_handlers
from main_bot.handlers.users.subs import register_subscribe_handlers

from main_bot.misc.init_commands import set_default_commands
from main_bot.misc.mailing import send_news
from main_bot.models.models import db

logger = logging.getLogger(__name__)


async def on_startup(dispatcher: Dispatcher):
    try:
        config = dispatcher.bot.get('config')
        await db.set_bind(f"postgresql://{config.db.user}:{config.db.password}@{config.db.host}:5432/{config.db.database}")
        await set_default_commands(dispatcher)
    except Exception as e:
        print(e)
        await db.pop_bind().close()


def register_all_handlers(dp):
    register_start_handlers(dp)
    register_admin_handlers(dp)
    register_news_handlers(dp)
    register_subscribe_handlers(dp)


def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info("Starting bot")
    config = load_config(".env")

    storage = MemoryStorage()
    bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp = Dispatcher(bot, storage=storage)

    bot['config'] = config

    register_all_handlers(dp)

    loop = asyncio.get_event_loop()
    loop.create_task(send_news(16000, bot))
    executor.start_polling(dp, on_startup=on_startup)


if __name__ == '__main__':
    try:
        main()
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")
    except Exception as e:
        logger.error(f"Bot stopped with error {e}")
        db.pop_bind().close()
