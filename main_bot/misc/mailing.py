import asyncio

from aiogram import Bot

from main_bot.misc.notifications.news_notify import news_notification


async def send_news(sleep_time, bot: Bot) -> None:
    while True:
        await asyncio.sleep(sleep_time)
        await news_notification(bot)
