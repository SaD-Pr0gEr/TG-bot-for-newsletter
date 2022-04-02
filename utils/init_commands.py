from aiogram import Dispatcher
from aiogram.types import BotCommand


async def set_default_commands(dp: Dispatcher):
    await dp.bot.set_my_commands([
        BotCommand("start", "Старт"),
        BotCommand("subscribe", "Подписка на рассылку"),
        BotCommand("unsubscribe", "Отписка от рассылки"),
        BotCommand("news", "Все новости"),
        BotCommand("allusers", "Все пользователи"),
        BotCommand("subscribers", "Все подписчики на рассылку"),
    ])
