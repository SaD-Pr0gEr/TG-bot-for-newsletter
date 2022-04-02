import asyncio

from notifications.news_notify import news_notification


async def send_news(sleep_time):
    while True:
        await asyncio.sleep(sleep_time)
        await news_notification()
