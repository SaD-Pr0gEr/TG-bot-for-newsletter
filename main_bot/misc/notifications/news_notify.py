from aiogram import Bot

from main_bot.misc.parse_news import ParseBleacherReport
from main_bot.models.models import Users


async def news_notification(bot: Bot) -> None:
    get_new = ParseBleacherReport().parse_posts()[-1]
    get_all_users = await Users.all_subscribers()
    for users in get_all_users:
        text = [
            f"{get_new['post_title']}: {get_new['link']}\n",
            f"Источник: {get_new['proof']}"
        ]
        await bot.send_message(
            users.user_id,
            "\n".join(text)
        )
